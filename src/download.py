import os
from kaggle.api.kaggle_api_extended import KaggleApi

def download_dataset():
    kaggle_dir = os.path.join(os.getcwd(), 'kaggle')
    os.environ['KAGGLE_CONFIG_DIR'] = kaggle_dir

    api = KaggleApi()
    api.authenticate()

    print("🔄 Downloading dataset dari Kaggle...")
    api.dataset_download_files(
        dataset='harisudhan411/phishing-and-legitimate-urls',  # Ganti sesuai dataset kamu
        path='data/raw',
        unzip=True
    )
    print("✅ Dataset berhasil diunduh dan diekstrak ke folder data/raw")

if __name__ == "__main__":
    download_dataset()
