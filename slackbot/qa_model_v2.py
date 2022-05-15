#!/usr/bin/env python
# coding: utf-8
"""
Created on Sun May 15 02:23:38 2022

@author: The Learning Machine Team
"""


import os
import re
import time
import json
import copy
import openai
import pandas as pd

import nltk
# nltk.download('stopwords')
# from nltk.corpus import stopwords
# from nltk.tokenize import word_tokenize
# from nltk.stem import WordNetLemmatizer

from subprocess import Popen, PIPE, STDOUT

# from haystack.utils import launch_es, print_documents
from haystack.document_stores import ElasticsearchDocumentStore
from haystack.nodes import RAGenerator, DensePassageRetriever
from haystack.pipelines import DocumentSearchPipeline


  
class DataLoader:
    def __init__(self, repo_root_dir):
        self.repo_root_dir = repo_root_dir
        self.dataset_dir = os.path.join(repo_root_dir, 'dataset')
        self.covid_json_path = os.path.join(self.dataset_dir, 'COVID-19 FAQs | Allianz Global Assistance.json')
        self.travel_json_path = os.path.join(self.dataset_dir, 'Travel Insurance FAQs | Allianz Global Assistance.json')
        self.terms_and_conditions_json_path = os.path.join(self.dataset_dir, 'Question_Answer_merged.json')
        self.tac_csv_path = os.path.join(self.dataset_dir, 'DataInChunk.csv')
        
        # self.stop_words = set(stopwords.words('german'))
        # self.stemmer = WordNetLemmatizer()
        
        
    def _preprocess(self, sent):
        # Remove all the special characters
        sent = re.sub(r'\W', ' ', sent)
        # remove all single characters
        sent = re.sub(r'\s+[a-zA-Z]\s+', ' ', sent)
        # Remove single characters from the start
        sent = re.sub(r'\^[a-zA-Z]\s+', ' ', sent) 
        # Substituting multiple spaces with single space
        sent = re.sub(r'\s+', ' ', sent, flags=re.I)
        # Removing prefixed 'b'
        sent = re.sub(r'^b\s+', '', sent)
        # Converting to Lowercase
        sent = sent.lower()
    
        text_tokens = word_tokenize(sent)
        sent = [self.stemmer.lemmatize(word)  for word in text_tokens if not word in self.stop_words]
        sent = (" ").join(sent)
    
        return sent
    
    
    def _load_qa_jsons(self):
        covid_data = pd.read_json(self.covid_json_path)
        travel_data = pd.read_json(self.travel_json_path)
        tac_df = pd.read_csv(self.tac_csv_path)
        
        tac_df['Question'] = ''
        tac_df = tac_df.rename(columns={'Data':'Answer'})
        tac_df = tac_df[['Question', 'Answer']]
        
        covid_df = pd.json_normalize(covid_data['FaqDocuments'])
        travel_df = pd.json_normalize(travel_data['FaqDocuments'])
        
        self.df = pd.concat([covid_df, travel_df, tac_df], axis=0)
        
        # self.df["Question"] = self.df['Question'].apply(self._preprocess)
        # self.df["Answer"] = self.df['Answer'].apply(self._preprocess)
        
        questions = self.df["Question"].values.tolist()
        answers = self.df["Answer"].values.tolist()
        
        df_ = copy.deepcopy(self.df)
        df_ = df_.rename(columns={"Answer":"text", "Question":"metadata"})
        df_.to_json (os.path.join(self.dataset_dir, 'qa_exported_jl.json'), orient='records', lines=True)

        return questions, answers
    
    
    def make_document(self):
        questions, answers = self._load_qa_jsons()
        docs = []
        for i in range(len(questions)):
            entry = {"meta" : {"question":''}, "content" : answers[i]}
            docs.append(entry)
        return docs
          


 
class HayStacker:
    def __init__(self, docs):
        self.docs = docs
        
        # self._start_elastic_search()
        self.document_store = self._build_doc_store()
        
    
    # @staticmethod
    # def _start_elastic_search():
    #     launch_es()


    @staticmethod
    def _build_doc_store():
        return ElasticsearchDocumentStore()
    
    
    def bulit_retriver(self, retriver_name="DPR"):
        if retriver_name == "DPR":
            self.retriever = DensePassageRetriever(
                document_store=self.document_store,
                query_embedding_model="facebook/dpr-question_encoder-single-nq-base",
                passage_embedding_model="facebook/dpr-ctx_encoder-single-nq-base",
                use_gpu=True,
                embed_title=True)
        return self.retriever


    def build_generator(self):
        self.generator = RAGenerator(
            model_name_or_path="facebook/rag-token-nq",
            use_gpu=False,
            top_k=1,
            max_length=200,
            min_length=2,
            embed_title=True,
            num_beams=2)
        return self.generator


    def compute_docs_embeddings(self):
        self.document_store.write_documents(self.docs)
        self.document_store.update_embeddings(self.retriever)


    def build_pipeline(self):
        self.pipe = DocumentSearchPipeline(self.retriever)
        return self.pipe
    
    
    def create_hs(self):
        self.retriever = self.bulit_retriver()
        self.generator = self.build_generator()
        self.pipe = self.build_pipeline()
        self.compute_docs_embeddings() ### ?
    
    
    def call_hs(self, query):
        res = self.pipe.run(query=query, params={"Retriever": {"top_k": 3}})
        print_documents(res, max_text_len=512)
        return res
    
 
class GPT3:
    def __init__(self, json_line_path):
        self.json_line_path = json_line_path
        
        opanai_api_key_path = "opanai_api_key.txt"
        openai.api_key_path = opanai_api_key_path
        
        self.opfilename = self._upload_data()
    
    
    def completion_api(self, query, info):
        TAG = "use the above information to answer the question"
        response = openai.Completion.create(
          engine="text-davinci-002",
          prompt=f"information:\n{info}\n\n\n{TAG}: {query}",
          temperature=0.7,
          max_tokens=256,
          top_p=1,
          frequency_penalty=0,
          presence_penalty=0)

        answer = str(response['choices'][0].to_dict()['text'])[2:]
        
        return answer

    
    def _upload_data(self, first_time=False):
        if first_time:
            opfile = openai.File.create(file=open("dataset/covid_exported_jl.json"), purpose='answers')
            opfilename = opfile.to_dict()['id']
        else:
            opfilename = 'file-UqMyZRjqTGYJ4OIO6iNRxWEc'
        return opfilename
        
    
    def answer_api(self, query):
        resp = openai.Answer.create(
            search_model="ada", 
            model="curie", 
            question=query, 
            file=self.opfilename, 
            examples_context="In 2017, U.S. life expectancy was 78.6 years.", 
            examples=[["What is human life expectancy in the United States?", "78 years."]], 
            max_rerank=10,
            max_tokens=10,
            stop=["\n", "<|endoftext|>"]
        )
        
        return resp['selected_documents'][-1]['text']
    
    
    def post_to_gpt3_completion(self, query, info):
        comp_ans = self.completion_api(query, info)
        return comp_ans
    
    
    def post_to_gpt3_answer(self, query):
        answ_ans = self.answer_api(query)
        return answ_ans


 
class HsResponder:
    def __init__(self, repo_root_dir):
        self.repo_root_dir = repo_root_dir
        self.dataset_dir = os.path.join(repo_root_dir, 'dataset')
        
        self.data_loader = DataLoader(repo_root_dir)
        self.docs = self.data_loader.make_document()
        
  
class QaPipeline:
    def __init__(self, repo_root_dir, model_name='hi'):
        self.repo_root_dir = repo_root_dir
        self.model_name = model_name
        self.dataset_dir = os.path.join(repo_root_dir, 'dataset')
        self.json_line_path = os.path.join(self.dataset_dir, 'qa_exported_jl.json')
    
        self.data_loader = DataLoader(repo_root_dir)
        self.docs = self.data_loader.make_document()
        
        if model_name == 'hs':
            self.haystacker = HayStacker(self.docs)
            self.haystacker.create_hs()
        elif model_name == 'gpt3':
            self.gpt3 = GPT3(self.json_line_path)
        else:
            self.haystacker = HayStacker(self.docs)
            self.haystacker.create_hs()
            self.gpt3 = GPT3(self.json_line_path)
        
        
    def _get_hs_response(self, query):
        hs_resp = self.haystacker.call_hs(query)
        return hs_resp
        
    def _get_gpt3_response(self, query, info=None):
        comp_ans = self.gpt3.post_to_gpt3_completion(query, info)
        answ_ans = self.gpt3.post_to_gpt3_answer(query)
        return comp_ans, answ_ans
        
    
    def prediction(self, query, info=None):
        if self.model_name == 'hs':
            hs_resp = self._get_hs_response(query)
            return hs_resp
        elif self.model_name == 'gpt3':
            comp_ans, answ_ans = self._get_gpt3_response(query, info)
            return comp_ans, answ_ans
        else:
            hs_resp = self._get_hs_response(query)
            
            info = ''
            for doc in hs_resp["documents"]:
                content = doc.content
                info += ' ' + content 
                
            comp_ans, answ_ans = self._get_gpt3_response(query, info)
            return hs_resp, comp_ans, answ_ans

def setup_responder():

    import os
    from subprocess import Popen, PIPE, STDOUT

    es_server = Popen(
        ["elasticsearch-7.9.2/bin/elasticsearch"], stdout=PIPE, stderr=STDOUT, preexec_fn=lambda: os.setuid(1)  # as daemon
    )

    repo_root_dir = ""
    model_name = "hi"
    qa_pipeline = QaPipeline(repo_root_dir, model_name)
    return qa_pipeline
 
def call_hs(qa_pipeline, query):
    hs_resp, comp_ans, answ_ans = qa_pipeline.prediction(query)
    print(hs_resp)
    print(comp_ans)
    return hs_resp
        
