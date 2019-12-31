"""
@Description This file aims to extract some features from text for 3D scene building
@Author Yuki Tang
@Date 2019-12-29
"""
import sys
import empath
from textblob import TextBlob
import re
import json
import paralleldots

paralleldots.set_api_key("6opLDf4BQzxKSeGWAfcPVV241zc9Huhn31mwtFy8pYo")

USERNAME = 'test'
DATE = '20191229'
FILENAME = r'{username}_{date}'.format(username = USERNAME, date = DATE)
TEXT_FILEPATH = r'./data/{filename}.txt'
JSON_FILEPATH = r'./data/{filename}.json'


def get_file():
    try:
        with open(TEXT_FILEPATH.format(filename = FILENAME),'rt') as textfile:
            text = textfile.read()
            # print (type(text))
            return text
    except OSError:
        pass


def overall_analysis(text):
    dict_data = {}
    
    blob = TextBlob(text)
    total = len(blob.sentences)
    dict_data['size'] = total
    
    tags = blob.tags
    nouns = []
    for tag in tags:
        if tag[1] == "NN":
            nouns.append(tag[0])    

    dict_data['noun'] = nouns
    dict_data['noun_phrases'] = blob.noun_phrases
    dict_data['words'] = blob.words
    dict_data['polarity'] = round(blob.sentiment.polarity,2)

    sentences = blob.sentences
    print(type(sentences))
    dict_data['sentences'] = []
    dict_sentence = dict_data['sentences']
    for i in range(len(sentences)):
        dict_sentence.append({})
        dict_sentence[i]['id'] = i
        dict_sentence[i]['content'] = str(sentences[i])
        dict_sentence[i]['polarity'] = round(sentences[i].sentiment.polarity,2)

    print(dict_data)    
    return dict_data

def save_json():
    text = get_file()    
    data = overall_analysis(text)    
    with open(JSON_FILEPATH,"w") as f:
        json.dump(data,f)
        print("Saved in json file")

if __name__ == "__main__":
    save_json()