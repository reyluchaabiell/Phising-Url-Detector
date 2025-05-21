import streamlit as st
from src.predict import predict_url

st.title("🔐 Phishing URL Detector")

url_input = st.text_input("Masukkan URL")

if st.button("Deteksi"):
    if url_input:
        result = predict_url(url_input)
        st.success(f"Hasil: {result}")
    else:
        st.warning("Tolong masukkan URL dulu.")
