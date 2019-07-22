# Flair_Detector
The project detects flairs using scikit learn models - Naive Bayes, Logistic Regression and Random Forest Classifier

Data Acquisition:
The project uses praw library to scrape data from reddit posts. The following properties of a post are considered to understand the data-
comments, title, url, username, date created. Per flair at most 200 posts are taken into the data.
Cleaning - nltk library is used to clean data using https://medium.com/@paritosh_30025/natural-language-processing-text-data-vectorization-af2520529cf7
Tasks followed - lowercase test, tokenization, removal of stopping words and punctuation. Data is stored as a csv file

Data Processing:
