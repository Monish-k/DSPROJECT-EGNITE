from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk import wordnet
from yake import yake
import pandas as pd
import csv

df = pd.read_csv("/Users/monish/code/Data-Science/DSWP-Egnite/Monish/week4/ResourceManager/total_data.txt",
                 sep=",")


def is_not_numeric(x):
    try:
        float(x)
        return False
    except:
        return True


doc = ""

for sentence in df["Title"]:
    doc += sentence + " "

word = word_tokenize(doc)
stop_words = set(stopwords.words("english"))
words = [x for x in word if (x not in stop_words and len(x) > 1 and is_not_numeric(x))]

lemma_word = ""
lemmar = wordnet.WordNetLemmatizer()

for word in words:
    lemma = lemmar.lemmatize(word)
    lemma_word += lemma + " "

lemma_extractor = yake.KeywordExtractor(lan="en", n=2, dedupLim=0.9, dedupFunc="seqm", windowsSize=1, top=200,
                                        features=None)
keywords = lemma_extractor.extract_keywords(lemma_word)

for kw in keywords:
    df[df["Title"].str.contains(kw[0])].to_csv(kw[0]+".csv",index=False)