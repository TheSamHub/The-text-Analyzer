import nltk
import pickle
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.ensemble import RandomForestClassifier
import csv
nltk.download('punkt')

df = pd.read_csv("sentiment140-subset.csv", nrows=30000)
vectorizer = TfidfVectorizer(max_features=1000)
vectors = vectorizer.fit_transform(df.text)
words_df = pd.DataFrame(vectors.toarray(), columns=vectorizer.get_feature_names())

X = words_df
y = df.polarity

forest = RandomForestClassifier(n_estimators=50)
forest.fit(X, y)
filename = 'finalized_model.pkl'
pickle.dump(forest, open(filename, 'wb'))