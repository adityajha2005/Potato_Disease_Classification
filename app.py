import streamlit as st
import requests
from PIL import Image
from io import BytesIO

API_URL = "http://localhost:8000/predict"

st.title("Potato Disease Classifier")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)
    
    img_bytes = uploaded_file.getvalue()  # Use getvalue() to read bytes

    st.write(f"Image data size: {len(img_bytes)} bytes")
    
    response = requests.post(API_URL, files={"file": ("filename", img_bytes, uploaded_file.type)})
    
    if response.status_code == 200:
        try:
            result = response.json()
            st.write(f"Prediction: {result['class']}")
            st.write(f"Confidence: {result['confidence']:.2f}")
        except ValueError:
            st.write("Error: Response content is not valid JSON.")
            st.write(response.text)
    else:
        st.write(f"Error: Unable to get prediction. Status code: {response.status_code}")
        st.write(response.text)
