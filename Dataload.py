from bs4 import BeautifulSoup
from nltk.corpus import stopwords
import re
import os
# import BeautifulSoup4


datafolder = "./webkb"
csvdata=open("./data/data2.csv", "w")
csvdata.write("data,category\n")
stop_words = set(stopwords.words("english"))

for category in os.listdir(datafolder):
    for uni in os.listdir(datafolder+"/"+category):
        for files in os.listdir(datafolder+"/"+category+"/"+uni):
            # print("---"+files)
            try:
                f=open(datafolder+"/"+category+"/"+uni+"/"+files,"r")
                filesrc = f.read().lower()
                if "<html>" not in filesrc or "<title>" not in filesrc:
                    continue
                filehtml=filesrc[filesrc.index("<"):]
                filetext = BeautifulSoup(filehtml, "html.parser").get_text()
                filewords = re.sub('[^a-z| +]', ' ', filetext)
                fileclean = filewords.split()
                filedata = [x for x in fileclean if x not in stop_words and len(x)>2]
                filefinal = " ".join(filedata)
                # csvdata.write(category + "," + uni + "," + filefinal + "\n")
                csvdata.write( filefinal + "," + category + "\n")
                f.close()
            except Exception as e:
                print("Unable to process file {0}/{1}/{2}".format(category,uni,files))
                print(str(e))
                continue
csvdata.close()
