"""
@Description This file aims to extract some features from text for 3D scene building
@Author Yuki Tang
@Date
"""
import sys
import empath
from textblob import TextBlob
import re
import json

USERNAME = 'test'
DATE = '20191229'
TEXT_FILEPATH = r'./text/{username}_{date}.txt'


def get_file():
    try:
        with open(TEXT_FILEPATH.format(username = USERNAME,date = DATE),'rt') as textfile:
            text = textfile.read()
            # print (type(text))
            return text
    except OSError:
        pass


def overall_analysis(text):
    pass

def split_text():
    pass

def split_analysis():
    pass

def split_word():
    pass

def save_json():
    pass



if __name__ == "__main__":
    get_file()