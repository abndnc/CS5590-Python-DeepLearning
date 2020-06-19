# SVM

# importing the libraries
import pandas as pd
from sklearn.svm import SVC, LinearSVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

# importing the data set
dataset = pd.read_csv('glass.csv')
X = dataset.drop('Type', axis=1)
y = dataset['Type'].values

# splitting the data set into the Training set and Test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0, stratify=y)

# fitting SVM to the Training set
svc = SVC()
svc.fit(X_train, y_train)

# predicting the Test set results
y_pred = svc.predict(X_test)

# calculating accuracy
acc_svc = round(svc.score(X_train, y_train) * 100, 2)

print("svm accuracy is:", acc_svc, "%")

print(classification_report(y_test, y_pred))

