
import re
import string
import pandas as pd
import numpy as np



def clean_text(text):
    #Make text lowercase, remove text in square brackets, remove links, remove punctuation
    #and remove words containing numbers
    #getting list with polish stop words

    stop_words_path = 'polishstopwords.txt'
    stop_words = pd.read_csv(stop_words_path, sep=" ", header=None)
    stop_words.columns = ["word"]
    #stop_words.head()
    stop_words = stop_words["word"].tolist()
    #print(stop_words)

    #lowecase
    text = str(text).lower()
    #remove text in square brackets
    text = re.sub('\[.*?\]', '', text)
    #remove links
    text = re.sub('https?://\S+|www\.\S+', '', text)
    #remove punctuation and words containing numbers
    text = re.sub('<.*?>+', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\n', '', text)
    text = re.sub('\w*\d\w*', '', text)
    #removing stop words
    tokens = []
    for token in text.split():
        if token not in stop_words:
                tokens.append(token)
    return " ".join(tokens)
    

#test = "hej, nie co tam i albo aczkolwiek, polska gola lewandowski"
#print(clean_text(test))
#text preprocessing
#dataset['description'] = dataset['description'].apply(lambda x:clean_text(x))