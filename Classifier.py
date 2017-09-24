# import csv
# datafile = "./data/Data.csv"
# with open(datafile, 'r') as f:
#     reader = csv.reader(f)
#
#     your_list = list(reader)
#
# print(your_list[0:5])

# import pandas as pd
# df = pd.from_csv()
# print(df[:3])
import nltk
import pandas as pd
import numpy as np
df=pd.read_csv(r".\data\Data2.csv")
# print(df[-1:])
train_set = df[:4300]
test_set = df[4300:]
classifier = nltk.NaiveBayesClassifier(train_set)
# df['split'] = np.random.randn(df.shape[0], 1)
# msk = np.random.rand(len(df)) <= 0.7
# train = df[msk]
# print(train)
# test = df[~msk]
# print(test)