# Naive Bayes

# importing the libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn import metrics
from sklearn.metrics import classification_report

# importing the data set
dataset = pd.read_csv('glass.csv')
X = dataset.drop('Type', axis=1)
y = dataset['Type'].values

# splitting the data set into the Training set and Test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0, stratify=y)


# fitting Naive Bayes to the Training set
classifier = GaussianNB()
classifier.fit(X_train, y_train)

# predicting the Test set results
y_pred = classifier.predict(X_test)

# calculating accuracy
acc = round(metrics.accuracy_score(y_test, y_pred) * 100, 2)

print("Naive Bayes accuracy is:", acc, "%")

print(classification_report(y_test, y_pred))