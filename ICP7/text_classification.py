from sklearn.datasets import fetch_20newsgroups
categories = ['alt.atheism', 'soc.religion.christian',
              'comp.graphics', 'sci.med']
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import SVC

# Original model (Naive Bayes)
twenty_train = fetch_20newsgroups(subset='train', shuffle=True)
tfidf_Vect = TfidfVectorizer()
X_train_tfidf = tfidf_Vect.fit_transform(twenty_train.data)
# print(tfidf_Vect.vocabulary_)
clf = MultinomialNB()
clf.fit(X_train_tfidf, twenty_train.target)
twenty_test = fetch_20newsgroups(subset='test', shuffle=True)
X_test_tfidf = tfidf_Vect.transform(twenty_test.data)
predicted = clf.predict(X_test_tfidf)
score = round(clf.score(X_test_tfidf, twenty_test.target) * 100, 2)
print("Original score:", score)

# SVM
twenty_train = fetch_20newsgroups(subset='train', categories=categories, shuffle=True)
tfidf_Vect = TfidfVectorizer()
X_train_tfidf = tfidf_Vect.fit_transform(twenty_train.data)
clf = SVC()
clf.fit(X_train_tfidf, twenty_train.target)
twenty_test = fetch_20newsgroups(subset='test', categories=categories, shuffle=True)
X_test_tfidf = tfidf_Vect.transform(twenty_test.data)
predicted = clf.predict(X_test_tfidf)
score = round(clf.score(X_test_tfidf, twenty_test.target) * 100, 2)
print("SVM:", score)

# change vectorizer
tfidf_Vect = TfidfVectorizer(ngram_range=(1,2))
X_train_tfidf = tfidf_Vect.fit_transform(twenty_train.data)
clf = SVC()
clf.fit(X_train_tfidf, twenty_train.target)
twenty_test = fetch_20newsgroups(subset='test', categories=categories, shuffle=True)
X_test_tfidf = tfidf_Vect.transform(twenty_test.data)
predicted = clf.predict(X_test_tfidf)
score = round(clf.score(X_test_tfidf, twenty_test.target) * 100, 2)
print('Bigram:',score)

# set argument
tfidf_Vect = TfidfVectorizer(stop_words='english')
X_train_tfidf = tfidf_Vect.fit_transform(twenty_train.data)
clf = SVC()
clf.fit(X_train_tfidf, twenty_train.target)
twenty_test = fetch_20newsgroups(subset='test', categories=categories, shuffle=True)
X_test_tfidf = tfidf_Vect.transform(twenty_test.data)
score = round(clf.score(X_test_tfidf, twenty_test.target) * 100, 2)
print('Stop Words:',score)