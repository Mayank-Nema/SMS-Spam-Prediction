import streamlit as st
import pickle
import nltk
import string
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

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
