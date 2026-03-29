# Emotion Detection Web App

This is a Flask-based web application that predicts human emotions from text using Machine Learning (SVM + TF-IDF).

## 🚀 Features
- Predicts emotions from text input
- Clean and simple UI
- Fast and lightweight model
- Docker support

## 🧠 Tech Stack
- Python
- Flask
- Scikit-learn
- NLP (TF-IDF, NLTK)

## 📂 Project Structure
emotion-app/
│
├── app.py
├── model.pkl
├── vectorizer.pkl
├── templates/
│     └── index.html
├── Dockerfile
├── requirements.txt
└── README.md

## ⚙️ Installation

```bash
pip install -r requirements.txt
python app.py