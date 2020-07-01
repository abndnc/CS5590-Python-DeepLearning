import requests
from bs4 import BeautifulSoup
import nltk
from nltk.stem.porter import *
from nltk.stem import WordNetLemmatizer
from nltk import trigrams

# download all depedencies of NLTK
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')
nltk.download('maxent_ne_chunker')
nltk.download('words')
nltk.download('punkt')

# get the web content
html_doc = requests.get('https://en.wikipedia.org/wiki/Google')
# scrap content using BeautifulSoup
soup = BeautifulSoup(html_doc.content, 'html.parser')

somelist = []

for link in soup.find_all('a'):
  somelist.append(link.get('href'))

with open('input.txt','w') as f:
  for listitem in somelist:
    f.write('%s\n' % listitem)

with open('input.txt', 'r') as f:
  data = f.read().replace('\n', '')
# tokenization
tokenization = nltk.word_tokenize(data)
print("Tokenization:", tokenization)
# pos
pos = nltk.pos_tag(tokenization)
print("POS:", pos)
# stemming
stemming  = PorterStemmer()
stem = ''
for w in tokenization:
  stem = stem + stemming.stem(w) + ' '
print("Stemming:", stem)
# lemmetization
lemmatizer = WordNetLemmatizer()
lemm = ''
for w in tokenization:
  lemm = lemm + lemmatizer.lemmatize(w) + ' '
print("Lemmetization:", lemm)
# trigram
trigram = trigrams(tokenization)
print("Trigram:")
for x in trigram:
    print(x)
# named identity recognition
named_e_r = nltk.ne_chunk(pos, binary=True)
print("Name Identity Recognition:", named_e_r)