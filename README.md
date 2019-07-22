# Flair_Detector
The project detects flairs using scikit learn models - Naive Bayes, Logistic Regression and Random Forest Classifier

Data Acquisition:
The project uses praw library to scrape data from reddit posts. The following properties of a post are considered to understand the data-
comments, title, url, username, date created. Per flair at most 200 posts are taken into the data.
Cleaning - nltk library is used to clean data using https://medium.com/@paritosh_30025/natural-language-processing-text-data-vectorization-af2520529cf7
Tasks followed - lowercase test, tokenization, removal of stopping words and punctuation. Data is stored as a csv file

Data Processing:
Data is converted into numerical form using CounterVectorization(). scikit learn's inbuilt python modules for Naive Bayes, Logistic regression and Random Forest are trained on 80 percent of data acquired and tested on rest 20 percent. Sources used #using https://www.datacamp.com/community/tutorials/naive-bayes-scikit-learn and https://www.dataquest.io/blog/sci-kit-learn-tutorial/
using https://towardsdatascience.com/logistic-regression-using-python-sklearn-numpy-mnist-handwriting-recognition-matplotlib-a6b31e2b166a
using https://towardsdatascience.com/multi-class-text-classification-model-comparison-and-selection-5eb066197568
Results:
  Naive Bayes - 0.52
  Logistic Regression - 0.72
  Random Forrest - 0.62
 Model obtained by Logisctic Regression is stored as joblib file for predicting flairs.
 
Prediction:
User submits URL of reddit post in the form. Logistic Regression model stored as LR.joblib is used to predict flair of the scrapped data from the entered url




