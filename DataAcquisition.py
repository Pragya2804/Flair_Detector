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
import csv

csv_write = open("FlairData.csv", 'w', newline='')
writer1 = csv.writer(csv_write)
writer1.writerow(["Flair", "Data"])


def clean(text):
    #removing html tags
    text2=BeautifulSoup(text,"html.parser").text
    #lower case the string
    text=text2.lower()
    #tokenize-split into words and removes punctuations
    words = list(token for token in RegexpTokenizer('\w+').tokenize(text))
    textset=set(words)
    textlist=list(textset)
    #removing stop words
    stoppers=set(stopwords.words('english'))
    unstopped=[]
    text=''
    for word in textlist:
        if(word not in stoppers):
            unstopped.append(word)
            text=text+word+" "
            
    return text

def generate(name, count, topics_dict, flair, flairsdict):
    for submission in name:
        try:
            if(count<200):
                l=[]
                topics_dict["flair"].append(flair)
                l.append(flair)
                title=clean(submission.title)
                topics_dict["title"].append(title)
                submission.comments.replace_more(limit=None)
                comment=''
                for top_level_comment in submission.comments:
                    comment+=top_level_comment.body+" "
                comment=clean(comment)
                topics_dict["comments"].append(comment)
                topics_dict["link"].append(submission.url)
                topics_dict["timestamp"].append(dt.datetime.fromtimestamp(submission.created))
                topics_dict["userhandle"].append(str(submission.author))
                topics_dict["all"].append(title+" "+comment+" "+submission.url+" "+str(submission.author))
                l.append(title+" "+comment+" "+submission.url+" "+str(submission.author))
                l.append(submission.created)
                l.append(dt.datetime.fromtimestamp(submission.created))
                writer1.writerow(l)
                count+=1
                print(flair, count)
                flairsdict[flair]+=1
        except:
            pass
    return
    

reddit = praw.Reddit(client_id='Enter client_id', \
                     client_secret='Enter client_secret number', \
                     user_agent='Flair Detector', \
                     username='Enter username', \
                     password='Enter password')

subreddit = reddit.subreddit('india')

flairs=["Political","Sports","Food","Non-political","AskIndia","Science & Technology","Policy & Economy","Finance & Business","Photography","Reddiquette","AMA"]
flairsdict={"Political":0, "Sports": 0, "Food": 0,"Non-political" : 0,"Reddiquette": 0,"AskIndia": 0,"Science & Technology":0,"Policy & Economy":0,"Finance & Business":0,"Photography":0,"AMA":0}


topics_dict = { "flair":[], \
               "title":[], \
                "comments":[], \
                "link":[], \
                "timestamp":[], "userhandle":[], "all":[]
                
              }

for flair in flairs:
    name = subreddit.search(flair, limit=200)
    count=0
    generate(name, 0, topics_dict, flair, flairsdict)
    
    
data=pd.DataFrame(topics_dict)
# data.to_csv('FlairDate.csv')

