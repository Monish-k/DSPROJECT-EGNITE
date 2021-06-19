from textblob import TextBlob
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import pandas as pd

df = pd.read_csv("/Users/monish/code/Data-Science/DSWP-Egnite/Monish/week4/KeyPharseExtraction/data.csv")

for text in df["Title"]:
    print(text, TextBlob(text).sentiment.polarity)

print("\n\n\n")

for text in df["Title"]:
    sid = SentimentIntensityAnalyzer()
    print(text, sid.polarity_scores(text))