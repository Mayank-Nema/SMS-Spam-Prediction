import streamlit as st
import pickle
import string
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import nltk
import os

NLTK_DATA_DIR = "/opt/render/nltk_data"

if not os.path.exists(NLTK_DATA_DIR):
    os.makedirs(NLTK_DATA_DIR)

nltk.data.path.append(NLTK_DATA_DIR)

def download_nltk_data():
    resources = ["punkt", "punkt_tab", "stopwords"]
    for resource in resources:
        try:
            nltk.data.find(resource)
        except LookupError:
            nltk.download(resource, download_dir=NLTK_DATA_DIR)

download_nltk_data()


ps=PorterStemmer()

def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    y = []
    for i in text:
        if i.isalnum():
            y.append(i)
    text = y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)

tfid= pickle.load(open('vectorizer.pkl', 'rb'))
model=pickle.load(open('model.pkl', 'rb'))

print("Vectorizer loaded:", type(tfid))
print("Model loaded:", type(model))

st.title("Email/SMS Classifier")
input_sms=st.text_input("Enter the message")

if st.button("Predict"):

    #1. preprocessing
    transform_sms=transform_text(input_sms)
    #2. vectorize
    vector_input=tfid.transform([transform_sms])
    #3. predict
    result=model.predict(vector_input)[0]
    #4. Display
    if result==1:
        st.header("Spam")
    else:
        st.header("Not Spam")
