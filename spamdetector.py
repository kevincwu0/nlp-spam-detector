from sklearn.naive_bayes import MultinomialNB
import pandas as pd
import numpy as np

#no need for pandas stuff so turn into raw matrix
data = pd.read_csv('spambase.data').as_matrix()

# split into train and test, different each time
np.random.shuffle(data)

X = data[:, :48]
Y = data[:, -1]

Xtrain = X[:-100,]
Ytrain = Y[:-100,]
Xtest = X[-100:,]
Ytest = Y[-100:,]

model = MultinomialNB()
model.fit(Xtrain, Ytrain)
print "Classification rate for NB:", model.score(Xtest, Ytest)

from sklearn.ensemble import AdaBoostClassifier

model = AdaBoostClassifier()
model.fit(Xtrain, Ytrain)
print "Classification rate for AdaBoostClassifier", model.score(Xtest, Ytest)
