from flask import Flask, request, render_template,jsonify
import pickle
import numpy as np
import pandas as pd
import json
import nltk
import pickle
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
nltk.download('punkt')
import nltk
from nltk.tokenize import word_tokenize
from collections import Counter
nltk.download('wordnet')      


from nltk.stem import WordNetLemmatizer 
from nltk.corpus import stopwords
nltk.download('stopwords')    


#For Gensim
import gensim
import string
from gensim import corpora
from gensim.corpora.dictionary import Dictionary
from nltk.tokenize import word_tokenize



app = Flask(__name__)
model = pickle.load(open('finalized_model.pkl', 'rb'))

def do_something(bookname,para):
   #bookname = bookname.upper()
   #para = para.upper()
   #combine = bookname + para
   a_list = nltk.tokenize.sent_tokenize(para)
   
   return a_list    
@app.route('/')
def home():
    return render_template("index.html")

@app.route('/success', methods =["GET", "POST"])
def successfull():
    if request.method == "POST":
       # getting input with name = fname in HTML form
       bookname = request.form.get("bookname")
       # getting input with name = lname in HTML form 
       para = request.form.get("para") 
       combine = do_something(bookname,para)
       combine.append(str(para))
       vectorizer = TfidfVectorizer(max_features=1000)
       #vectors = vectorizer.fit_transform(df.text)
       #words_df = pd.DataFrame(vectors.toarray(), columns=vectorizer.get_feature_names())
       
       yes = pd.DataFrame({'content': combine})
       yes_vectors = vectorizer.transform(yes.content)
       yes_words_df = pd.DataFrame(yes_vectors.toarray(), columns=vectorizer.get_feature_names())
       yes['Sentiment Score'] = forest.predict_proba(yes_words_df)[:,1]
       yes.values.tolist()
       # for topic code is below 
       text1=para
       tokens = word_tokenize(text1)
       lowercase_tokens = [t.lower() for t in tokens]
       bagofwords_1 = Counter(lowercase_tokens)
       alphabets = [t for t in lowercase_tokens if t.isalpha()]
       words = stopwords.words("english")
       stopwords_removed = [t for t in alphabets if t not in words]
       lemmatizer = WordNetLemmatizer()
       lem_tokens = [lemmatizer.lemmatize(t) for t in stopwords_removed]
       bag_words = Counter(lem_tokens)
       topic = bag_words.most_common(6)[0][0]
    return ("<p>" + "</p><p>".join(yes) + "</p>") +"\n" +"The topic suggested is :" + str(topic).upper()
    #return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)
