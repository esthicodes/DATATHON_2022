#!/usr/bin/env python
# coding: utf-8

# ## Install dependencies

# In[1]:


# Install the latest release of Haystack in your own environment
get_ipython().system(' pip install farm-haystack')

# Install the latest master of Haystack
get_ipython().system('pip install --upgrade pip')
get_ipython().system('pip install wget')

get_ipython().system('pip install git+https://github.com/deepset-ai/haystack.git#egg=farm-haystack[colab]')


# In[5]:


get_ipython().system('pip install faiss')
# !sudo apt-get install libomp-dev


# ## Imports

# In[6]:


from haystack.document_stores import ElasticsearchDocumentStore
from haystack.document_stores import InMemoryDocumentStore

from haystack.nodes import EmbeddingRetriever, BM25Retriever, ElasticsearchRetriever
import pandas as pd
import requests


# ### Start an Elasticsearch server
# You can start Elasticsearch on your local machine instance using Docker. If Docker is not readily available in your environment (eg., in Colab notebooks), then you can manually download and execute Elasticsearch from source.

# In[7]:


# Recommended: Start Elasticsearch using Docker via the Haystack utility function
# from haystack.utils import launch_es

# launch_es()


# In[8]:


# In Colab / No Docker environments: Start Elasticsearch from source
get_ipython().system(' wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-7.9.2-linux-x86_64.tar.gz -q')
get_ipython().system(' tar -xzf elasticsearch-7.9.2-linux-x86_64.tar.gz')
get_ipython().system(' chown -R daemon:daemon elasticsearch-7.9.2')

import os
from subprocess import Popen, PIPE, STDOUT

es_server = Popen(
    ["elasticsearch-7.9.2/bin/elasticsearch"], stdout=PIPE, stderr=STDOUT, preexec_fn=lambda: os.setuid(1)  # as daemon
)
# wait until ES has started
get_ipython().system(' sleep 30')


# ### Init the DocumentStore
# In contrast to Tutorial 1 (extractive QA), we:
# 
# * specify the name of our `text_field` in Elasticsearch that we want to return as an answer
# * specify the name of our `embedding_field` in Elasticsearch where we'll store the embedding of our question and that is used later for calculating our similarity to the incoming user question
# * set `excluded_meta_data=["question_emb"]` so that we don't return the huge embedding vectors in our search results

# In[9]:


from haystack.document_stores import ElasticsearchDocumentStore


# ### Create a Retriever using embeddings
# Instead of retrieving via Elasticsearch's plain BM25, we want to use vector similarity of the questions (user question vs. FAQ ones).
# We can use the `EmbeddingRetriever` for this purpose and specify a model that we use for the embeddings.

# In[10]:


from haystack import Pipeline
from haystack.utils import launch_es


# ### Prepare & Index FAQ data
# We create a pandas dataframe containing some FAQ data (i.e curated pairs of question + answer) and index those in elasticsearch.
# Here: We download some question-answer pairs related to COVID-19

# In[ ]:





# ### Ask questions
# Initialize a Pipeline (this time without a reader) and ask questions

# In[12]:


# from google.colab import files
# uploaded = files.upload()


# In[13]:


from typing import List
import requests
import pandas as pd
from haystack import Document
from haystack.document_stores import FAISSDocumentStore
from haystack.nodes import RAGenerator, DensePassageRetriever
from haystack.utils import fetch_archive_from_http
import faiss


# In[ ]:


document_store = ElasticsearchDocumentStore()


# In[ ]:


# Initialize DPR Retriever to encode documents, encode question and query documents
retriever = DensePassageRetriever(
    document_store=document_store,
    query_embedding_model="facebook/dpr-question_encoder-single-nq-base",
    passage_embedding_model="facebook/dpr-ctx_encoder-single-nq-base",
    use_gpu=True,
    embed_title=True,
)

# Initialize RAG Generator
generator = RAGenerator(
    model_name_or_path="facebook/rag-token-nq",
    use_gpu=False,
    top_k=1,
    max_length=200,
    min_length=2,
    embed_title=True,
    num_beams=2,
)


# In[ ]:


import io
import json

filename = list(uploaded.keys())[0]
df = pd.read_json(filename)


with open(filename) as json_file:
    data = json.load(json_file)

qas = data["FaqDocuments"]
questions = [sample["Question"] for sample in qas]
answers = [sample["Answer"] for sample in qas]

# Get embeddings for our questions from the FAQs


#q_embeddings = retriever.embed_queries(texts=questions)
# q_embeddings = [q for q in questions]
# df = df.rename(columns={"question": "content"})
docs = []
for i in range(len(questions)):
  #docs_to_index[i] = {"embedding":q_embeddings[i], "question" : questions[i], "answer" : answers[i]}
  entry = {"meta" : {"question":questions[i]}, "content" : answers[i]}
  docs.append(entry)

# Convert Dataframe to list of dicts and index them in our DocumentStore
#docs_to_index = df.to_dict(orient="records")
document_store.write_documents(docs)
document_store.update_embeddings(retriever)


# In[ ]:


filename


# In[ ]:


print(docs[0]["content"])


# In[ ]:


from haystack.utils import print_documents
from haystack.pipelines import DocumentSearchPipeline

p_retrieval = DocumentSearchPipeline(retriever)
res = p_retrieval.run(query="I am worried about COVID-19 impacting a trip I have scheduled or plan to schedule. Should I buy an Allianz travel protection plan to cover me in case COVID-19 impacts my trip", params={"Retriever": {"top_k": 2}})
print_documents(res, max_text_len=512)


# In[ ]:


docs = [doc.content for doc in res['documents']]
docs[0]


# ## GPT-3

# In[ ]:


# !pip install openai


# In[ ]:


import openai
opanai_api_key_path = "opanai_api_key.txt"
openai.api_key_path = opanai_api_key_path


# In[ ]:


INFO = "COVID-19 is a known and evolving epidemic that is impacting travel worldwide, with continued spread and impacts expected.  Our travel protection plans do not generally cover losses directly or indirectly related to known, foreseeable, or expected events, epidemics, government prohibitions, warnings, or travel advisories, or fear of travel. However, we are pleased to announce the introduction of our Epidemic Coverage Endorsement to certain plans purchased on or after March 6, 2021.  This endorsement adds certain new covered reasons related to epidemics (including COVID-19) to some of our most popular insurance plans.  Please see the below FAQ section on “Epidemic Coverage Endorsement” for more information.  Note, the Epidemic Coverage Endorsement may not be available for all plans or in all jurisdictions.  To see if your plan includes this endorsement, please look for “Epidemic Coverage Endorsement” on your Declarations of Coverage or Letter of Confirmation. Additionally, in response to the ongoing public health and travel crisis, we are temporarily extending certain claims accommodations as follows*: 1. For plans that do not include the Epidemic Coverage Endorsement, we are temporarily accommodating claims for the following:  Emergency medical care for an insured who becomes ill with COVID-19 while on their trip (if your plan includes the Emergency Medical Care benefit) Trip cancellation and trip interruption if an insured, or that insured’s traveling companion or family member, becomes ill with COVID-19 either before or during the insured’s trip (if your plan includes Trip Cancellation or Trip Interruption benefits, as applicable)  2. If an insured or their traveling companion become ill with COVID-19 while on their trip, that insured will not be subject to the Trip Interruption benefit’s five-day maximum limit for additional accommodation and transportation expenses (however, the maximum daily limit for such expenses and the maximum Trip Interruption benefit limit still apply). These temporary accommodations are strictly applicable to COVID-19 and are only available to customers whose plan includes the applicable benefit.  These accommodations apply to plans currently in effect but may not apply to plans purchased in the future, so please refer to our Coverage Alert for the most up to date information before purchasing."


# In[ ]:


TAG = "use the above information to answer the question"


# In[ ]:


QUESTION = "I am worried about COVID-19 impacting a trip I have scheduled or plan to schedule. Should I buy an Allianz travel protection plan to cover me in case COVID-19 impacts my trip"


# In[ ]:


response = openai.Completion.create(
  engine="text-davinci-002",
  prompt=f"information:\n{INFO}\n\n\n{TAG}: {QUESTION}",
  temperature=0.7,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)


# In[ ]:


str(response['choices'][0].to_dict()['text'])[2:]


# In[ ]:


opfile = openai.File.create(file=open("/content/exported_jl.json"), purpose='answers')


# In[ ]:


opfilename = opfile.to_dict()['id']


# In[ ]:


resp = openai.Answer.create(
    search_model="ada", 
    model="curie", 
    question=QUESTION, 
    file=opfilename, 
    examples_context="In 2017, U.S. life expectancy was 78.6 years.", 
    examples=[["What is human life expectancy in the United States?", "78 years."]], 
    max_rerank=10,
    max_tokens=10,
    stop=["\n", "<|endoftext|>"]
)


# In[ ]:


resp.to_dict()


# In[ ]:


resp.keys()


# In[ ]:


resp['selected_documents'][-1]['text']


# In[ ]:




