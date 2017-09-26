import nltk
import pandas as pd
import numpy as np
from nltk.tokenize import word_tokenize

df=pd.read_csv(r".\data\data1.txt")

mt = df['data'].tolist()

all_words = set()
for x in mt:
    for y in x.split():
        # for y in x.split():
        all_words.add(y)

def find_features(f):
    words=set(f.split())
    features={}
    for w in all_words:
        features[w] = (w in words)
    return features

vdata = df[df.category!='other']
featuresets = []
for a in range(vdata.shape[0]):
    featuresets.append((find_features(vdata.iloc[a][0]),vdata.iloc[a][1]))

train_set = featuresets[:4300]
test_set = featuresets[4300:]
classifier = nltk.NaiveBayesClassifier.train(train_set)

print("accuracy: ", nltk.classify.accuracy(classifier,test_set))
