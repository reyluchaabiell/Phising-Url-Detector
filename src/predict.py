import joblib
import os
import sys
import pandas as pd

# Tambahkan path agar bisa import extract_features
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.feature_extraction import extract_features

def load_model():
    model_path = os.path.join('models', 'phishing_url_model.pkl')
    return joblib.load(model_path)

def predict_url(url):
    model = load_model()
    features = extract_features(url)
    df = pd.DataFrame([features])
    prediction = model.predict(df)[0]
    return "Phishing" if prediction == 1 else "Aman"

if __name__ == '__main__':
    user_input = input("Masukkan URL untuk dicek: ")
    result = predict_url(user_input)
    print(f"🔍 Hasil Deteksi: {result}")
