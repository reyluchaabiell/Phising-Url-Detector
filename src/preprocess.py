import pandas as pd

def load_data(path="data/raw/new_data_urls.csv"):
    df = pd.read_csv(path)
    print("📊 Data Loaded:")
    print(df.head(), "\n")
    print("ℹ️ Info:")
    print(df.info(), "\n")
    print("🔢 Descriptive Stats:")
    print(df.describe(include='all'))
    return df

if __name__ == "__main__":
    df = load_data()

def check_clean(df):
    print("❌ Missing values per column:")
    print(df.isnull().sum(), "\n")
    print("🔄 Duplicate rows:", df.duplicated().sum())
    df = df.drop_duplicates().reset_index(drop=True)
    df = df.dropna(subset=['url'])

import tldextract
import re

def extract_features(df):
    df['url_length'] = df['url'].apply(len)
    df['has_https'] = df['url'].apply(lambda x: int(x.startswith('https')))
    df['dot_count'] = df['url'].apply(lambda x: x.count('.'))
    df['has_ip'] = df['url'].apply(lambda x: int(bool(re.search(r'\d+\.\d+\.\d+\.\d+', x))))
    df['double_slash_pos'] = df['url'].apply(lambda x: x.find('//', 8))  # setelah protocol
    df['domain'] = df['url'].apply(lambda x: tldextract.extract(x).domain)
    return df
df.to_csv("data/processed/processed_urls.csv", index=False)
print("✅ Processed data saved to data/processed/processed_urls.csv")


