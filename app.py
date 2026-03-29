from flask import Flask, render_template, request
import pickle

# load model
model = pickle.load(open('model.pkl', 'rb'))
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))

app = Flask(__name__)

# preprocess function (same as yours)
import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

stop_words = set(stopwords.words('english'))

def preprocess(text):
    text = str(text).lower()
    text = re.sub(r'[^a-zA-Z]', ' ', text)
    words = word_tokenize(text)
    words = [w for w in words if w not in stop_words]
    return " ".join(words)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    text = request.form['text']
    clean_text = preprocess(text)

    vector = vectorizer.transform([clean_text])
    prediction = model.predict(vector)[0]

    emotions = {
        0: "Sadness",
        1: "Joy",
        2: "Love",
        3: "Anger",
        4: "Fear",
        5: "Surprise"
    }

    result = emotions.get(prediction, "Unknown")

    return render_template('index.html', prediction_text=result)

if __name__ == '__main__':
    app.run(debug=True)