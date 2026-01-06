# SMS-Spam-Prediction :
This project is a ML–based SMS Spam Detection system that classifies  SMS messages as Spam or Not Spam . The system uses NLP techniques to clean and transform text data and applies  ML models to achieve accurate classification.  The model is integrated into a Streamlit , allowing users to enter an SMS message and instantly get a prediction.

🎯 Problem Statement :
Spam messages such as promotional offers, lottery winnings, and phishing links are common and can mislead users.
The goal of this project is to automatically detect spam SMS messages using machine learning and text analysis.

🧠Approach & Workflow :
1. Data Loading & Cleaning
   - Removed unnecessary columns and duplicate messages.
   - Encoded target labels (Spam / Ham).
     
2. Text Preprocessing (NLP)
   - Converted text to lowercase.
   - Tokenized sentences into words.
   - Removed stopwords and punctuation.
   - Applied stemming to reduce words to their root form.
     
3. Feature Extraction
   - Used TF-IDF Vectorization to convert text into numerical features.

4. Model Training & Evaluation
   - Trained multiple models:
      * Naive Bayes
      * Support Vector Machine (SVM)
      * Logistic Regression
      * Extra Trees Classifier
   - Compared performance using accuracy and precision.
     
5. Ensemble Learning
   - Implemented a Voting Classifier to combine predictions from multiple models.

6. Deployment
   - Saved trained model and vectorizer using pickle.
   - Built a Streamlit web app for real-time SMS classification.
     
------------------------------------------------------------------------------------------------------------------------------------------------

🛠️ Technologies Used : 

. Python
. Pandas & NumPy
. NLTK (Natural Language Toolkit)
. Scikit-learn
. TF-IDF Vectorizer
. Streamlit
. Pickle


🔗 Live Demo: https://sms-spam-prediction-magp.onrender.com

⚠️ Note: Web Service may take up to 1 minute to load due to free hosting cold start.
