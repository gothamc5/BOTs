from bs4 import BeautifulSoup
import re
import os

datafolder = "./webkb"
csvdata=open("./data/data2.csv", "w")
csvdata.write("category,university,data ")
stopwords = ["and","the","but","for","are","was"]

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
                filetext = BeautifulSoup(filehtml, "html5lib").get_text()
                filewords = re.sub('[^a-z| +]', ' ', filetext)
                fileclean = filewords.split()
                filedata = [x for x in fileclean if x not in stopwords and len(x)>2]
                filefinal = " ".join(filedata)
                # csvdata.write(category + "," + uni + "," + filefinal + "\n")
                csvdata.write( filefinal + "," + category + "\n")
                f.close()
            except Exception:
                print("Unable to read file {0}/{1}/{2}".format(category,uni,files))
                continue
csvdata.close()


# import collections
# counter = collections.Counter(fileclean)
# print(counter)
