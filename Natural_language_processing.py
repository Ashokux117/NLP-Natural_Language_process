# -*- coding: utf-8 -*-
"""
Created on Wed Jul 30 12:15:04 2025

@author: DELL
"""
# Importing the libraries
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 

# importing dataset
dataset = pd.read_csv(r"C:\Users\DELL\Downloads\Restaurant_Reviews.tsv",delimiter='\t',quoting =3)
dataset
  
# Cleaning the texts
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

corpus = []

for i in range(0,1000):
    review = re.sub('[^a-zA-Z]', ' ',dataset['Review'][i])
    review = review.lower()
    review = review.split()
    ps = PorterStemmer()
    review = [ps.stem(word) for word in review if not word in set(stopwords.words('english'))]
    review =' '.join(review)
    corpus.append(review)


# Cleaning the  bag of word models
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer()
x = cv.fit_transform(corpus).toarray()
y = dataset.iloc[:,1].values

# spliting the datast into trainin set and testing set 
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x, y, test_size=0.20, random_state=0)

# Future scalling  
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
x = sc.fit_transform(x_train)
y = sc.transform (x_test)

# Random forest  classifier 
from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(n_estimators=10,criterion ='entropy',random_state =0) 
classifier.fit(x_train,y_train) 



# Decision Tree classifier model use 
#from sklearn.tree import DecisionTreeClassifier
#classifier =  DecisionTreeClassifier()
#classifier.fit(x_train,y_train)

# predicting the test set result
y_pred = classifier.predict(x_test)

# making the confusion matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test,y_pred)
print(cm)

from sklearn.metrics import accuracy_score
ac = accuracy_score(y_test,y_pred)

bais = classifier.score(x_train,y_train)
bais

variance = classifier.score(x_test,y_test) 
variance 




