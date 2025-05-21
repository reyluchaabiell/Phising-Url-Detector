import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import joblib
import os
from feature_extraction import extract_features



def main():
    # 1. Baca data
    data_path = os.path.join('data', 'processed', 'processed_urls.csv')
    data = pd.read_csv(data_path)


    # 2. Ekstrak fitur dari URL
    extracted_features = data['url'].apply(extract_features)
    features_df = pd.DataFrame(list(extracted_features))


    # 3. Siapkan label
    X = features_df
    y = data['status']

    # 4. Split data train-test
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # 5. Latih model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # 6. Prediksi dan evaluasi
    y_pred = model.predict(X_test)
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print("Precision:", precision_score(y_test, y_pred))
    print("Recall:", recall_score(y_test, y_pred))
    print("F1 Score:", f1_score(y_test, y_pred))

    # 7. Simpan model
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    model_path = os.path.join(BASE_DIR, 'models', 'phishing_url_model.pkl')
    os.makedirs(os.path.dirname(model_path), exist_ok=True)
    joblib.dump(model, model_path)
    print(f"✅ Model disimpan di: {model_path}")

if __name__ == '__main__':
    main()
