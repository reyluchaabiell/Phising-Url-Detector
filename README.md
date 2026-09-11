Phishing-URL-Detector

Mini project deteksi phishing URL menggunakan Machine Learning.

✨ Deskripsi

Proyek ini bertujuan membangun sistem deteksi URL phishing berbasis Machine Learning. Mulai dari pengunduhan dataset, preprocessing, feature engineering, pelatihan model, hingga antarmuka deteksi interaktif.

📁 Struktur Proyek

```text
phising-url-detector/
├── data/                    # Data asli dan hasil preprocessing
│   ├── raw/                 # Dataset mentah (Kaggle)
│   │   └── new_data_urls.csv
│   └── processed/           # Data setelah preprocessing
│       └── processed_urls.csv
├── models/                  # Model ML tersimpan
│   └── phishing_url_model.pkl
├── src/                     # Kode sumber aplikasi
│   ├── download.py          # Unduh dataset dari Kaggle
│   ├── preprocess.py        # Bersihkan & ekstrak fitur awal
│   ├── feature_extraction.py# Ekstraksi fitur URL
│   ├── train.py             # Latih model dan simpan hasil
│   └── predict.py           # Fungsi prediksi URL
├── app.py                   # Antarmuka Streamlit untuk deteksi interaktif
├── requirements.txt         # Daftar pustaka Python yang dibutuhkan
└── README.md                # Dokumentasi (file ini)

🚀 Langkah Instalasi

Clone repository

git clone https://github.com/reyluchaabiell/Phising-Url-Detector.git
cd Phising-Url-Detector

Buat virtual environment

python3 -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate   # Windows

Instal dependency

pip install -r requirements.txt

🗂️ Alur Kerja

Download Dataset

Jalankan src/download.py untuk mengunduh dataset mentah dari Kaggle.

Dataset tersimpan di data/raw/.

python src/download.py

Preprocessing

Bersihkan data:

Hapus duplikat dan baris kosong.

Tampilkan ringkasan statistik.

Simpan data bersih di data/processed/processed_urls.csv.

python src/preprocess.py

Feature Engineering

Ekstrak fitur URL seperti panjang URL, jumlah titik, kehadiran https, angka, dan domain.

Kode ada di src/feature_extraction.py.

Training Model

Jalankan src/train.py untuk melatih model RandomForest.

Model dievaluasi menggunakan akurasi, precision, recall, dan F1 score.

Model tersimpan di models/phishing_url_model.pkl.

python src/train.py

Prediksi URL Baru

Script src/predict.py memuat model dan fungsi predict_url(url).

Gunakan untuk mengecek URL satu per satu di CLI.

python src/predict.py

Antarmuka Interaktif

Gunakan Streamlit lewat app.py untuk UI web sederhana.

Jalankan dengan:

streamlit run app.py

Masukkan URL, klik "Deteksi", dan lihat hasilnya.

📊 Evaluasi Model

Setelah pelatihan, model menunjukkan performa:

Accuracy: ~80%

Precision: ~78%

Recall: ~85%

F1 Score: ~81%

🔮 Pengembangan Selanjutnya

Tambahkan lebih banyak fitur URL (e.g., panjang path, query parameters).

Coba model lain seperti Logistic Regression, XGBoost.

Buat REST API dengan Flask/FastAPI.

Distribusikan ke platform hosting (Streamlit Cloud, Heroku).

Tambahkan logging dan histori prediksi.

AUTHOR
Reylucha Biel
