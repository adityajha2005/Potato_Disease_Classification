import streamlit as st
import requests
from PIL import Image

API_URL = "http://localhost:8000/predict"

st.sidebar.title("Options")
st.sidebar.text("Upload an image to get predictions.")

st.markdown("# Potato Disease Classifier")
st.markdown("Upload a potato leaf image to detect any diseases and get the prediction.")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
    img_bytes = uploaded_file.getvalue()

    st.write(f"Image data size: {len(img_bytes)} bytes")
    
    with st.spinner("Processing..."):
        response = requests.post(API_URL, files={"file": ("filename", img_bytes, uploaded_file.type)})
        
        if response.status_code == 200:
            try:
                result = response.json()
                st.write(f"**Prediction:** {result['class']}")
                st.write(f"**Confidence:** {result['confidence'] * 100:.2f}%")
            except ValueError:
                st.write("Error: Response content is not valid JSON.")
                st.write(response.text)
        else:
            st.write(f"Error: Unable to get prediction. Status code: {response.status_code}")
            st.write(response.text)

st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("**Created by Aditya**")
