import lxml
import nltk
from nltk.corpus import stopwords
import praw
import pandas as pd
import datetime as dt
from bs4 import BeautifulSoup
from nltk.tokenize import word_tokenize
from nltk.tokenize import RegexpTokenizer
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB,MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn import metrics
from sklearn.linear_model import LogisticRegression
from joblib import dump, load
import csv



reddit = praw.Reddit(client_id='Enter client_id', \
                     client_secret='Enter Client Secret number', \
                     user_agent='Flair Detector', \
                     username='Enter username', \
                     password='Enter password')
subreddit = reddit.subreddit('india')

clf=load('LR.joblib')


def clean(text):
    text2=BeautifulSoup(text,"html.parser").text 	#removing html tags
    text=text2.lower()								#lower case the string
    words = list(token for token in RegexpTokenizer('\w+').tokenize(text)) #tokenize-split into words and removes punctuations
    textset=set(words)
    textlist=list(textset)
    stoppers=set(stopwords.words('english'))		#removing stop words
    unstopped=[]
    text=''
    for word in textlist:
        if(word not in stoppers):
            unstopped.append(word)
            text=text+word+" "
            
    return text


# using https://praw.readthedocs.io/en/latest/code_overview/models/submission.html
def output(Url):
	submission=reddit.submission(url=Url)
	title=clean(submission.title)
	submission.comments.replace_more(limit=None)
	comment=''
	for top_level_comment in submission.comments:
		comment+=top_level_comment.body+" "
	comment=clean(comment)
	query = (title+" "+comment+" "+submission.url+" "+str(submission.author))
	query=[query]
	ans=clf.predict(query)
	return ans[0]