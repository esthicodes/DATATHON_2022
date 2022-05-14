from bs4 import BeautifulSoup
import json
import requests

url = "https://www.allianztravelinsurance.com/covid-19-faq.htm"
file_name = "COVID-19 FAQs | Allianz Global Assistance"
# url = "https://www.allianztravelinsurance.com/faq.htm"
# file_name = "Travel Insurance FAQs | Allianz Global Assistance"

r = requests.get(url)
encoding = r.encoding if 'charset' in r.headers.get(
    'content-type', '').lower() else "utf-8"
parser = "html.parser"

soup = BeautifulSoup(r.content, parser, from_encoding=encoding)

dataset = []

questions_div = soup.find("div", class_="questions")

for e in questions_div.find_all("ul", {"class": ["category1", "category2", "category3", "category4"]}):
    # Get the question and the answer
    question_li = e.find("li", class_="quest")
    answer_li = e.find("li", class_="ans")
    question = question_li.get_text()
    answer = answer_li.get_text()

    # Make some data cleaning
    question = question.replace("+-", "")
    answer = answer.replace("+-", "")
    question = question.strip()
    answer = answer.strip()

    dataset.append({
        "Question": question,
        "Answer": answer
    })

jsonFile = {
    "SchemaVersion": 1,
    "FaqDocuments": dataset
}

with open('../dataset/' + file_name + '.json', 'w') as f:
    json.dump(jsonFile, f, indent=2)

with open('../dataset/' + file_name + '.html', 'w') as f:
    f.write(soup.prettify())
