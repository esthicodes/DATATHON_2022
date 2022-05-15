# -*- coding: utf-8 -*-
"""
Created on Sun May 15 02:42:37 2022

@author: The Learning Machine Team
"""

import pandas as pd

file_path = "dataset/COVID-19 FAQs | Allianz Global Assistance.json"
data = pd.read_json(file_path)
df = pd.json_normalize(data['FaqDocuments'])
df = df.rename(columns={"Answer":"text", "Question":"metadata"})


df.to_json (r'dataset/covid_exported_jl.json',orient='records', lines=True)
