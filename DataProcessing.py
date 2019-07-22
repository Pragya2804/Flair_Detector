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
from sklearn.ensemble import RandomForestClassifier
import csv



data = pd.read_csv("FlairData - Copy.csv",encoding = "ISO-8859-1") 

#using https://www.datacamp.com/community/tutorials/naive-bayes-scikit-learn and https://www.dataquest.io/blog/sci-kit-learn-tutorial/

X_train, X_test, y_train, y_test = train_test_split(data.Data, data.Flair, test_size=0.25,random_state=109)


# using https://towardsdatascience.com/logistic-regression-using-python-sklearn-numpy-mnist-handwriting-recognition-matplotlib-a6b31e2b166a
# using https://towardsdatascience.com/multi-class-text-classification-model-comparison-and-selection-5eb066197568


gnb = Pipeline([('vect', CountVectorizer()),
                 ('clf', MultinomialNB()),
                ])
gnb.fit(X_train, y_train)
y_pred = gnb.predict(X_test)
print("accuracy - ",metrics.accuracy_score(y_test, y_pred))
dump(gnb, 'NB.joblib')



LR = Pipeline([('vect', CountVectorizer()),
              ('clf', LogisticRegression(n_jobs=1, C=1e5)),
             ])
LR.fit(X_train, y_train)
y_pred = LR.predict(X_test)
print('accuracy - ' , metrics.accuracy_score(y_pred, y_test))
dump(LR, 'LR.joblib')



RF = Pipeline([('vect', CountVectorizer()),
              ('clf', RandomForestClassifier(n_estimators = 1000, random_state = 42)),
             ])
RF.fit(X_train, y_train)
y_pred = RF.predict(X_test)
print('accuracy - ', metrics.accuracy_score(y_pred, y_test))
dump(RF, 'RF.joblib')
