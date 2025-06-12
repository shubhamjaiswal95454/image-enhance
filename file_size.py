import streamlit as st
import cv2
from PIL import Image
import numpy as np
import io

# Function to enhance/upscale the image
def enhance_image(image, scale_percent=150):
    # Convert the PIL image to a CV2 image
    cv2_image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    width = int(cv2_image.shape[1] * scale_percent / 100)
    height = int(cv2_image.shape[0] * scale_percent / 100)
    dim = (width, height)
    # Resize image
    resized_image = cv2.resize(cv2_image, dim, interpolation=cv2.INTER_CUBIC)
    # Convert back to PIL image
    enhanced_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB)
    return Image.fromarray(enhanced_image)

# Streamlit app
st.title("Image Enhancer and Upscaler")

# Image upload
uploaded_image = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

if uploaded_image is not None:
    # Display original image
    original_image = Image.open(uploaded_image)
    st.subheader("Original Image")
    st.image(original_image, use_column_width=True)

    # Enhance image
    enhanced_image = enhance_image(original_image)

    # Display enhanced image
    st.subheader("Enhanced Image")
    st.image(enhanced_image, use_column_width=True)

    # Download enhanced image
    buf = io.BytesIO()
    enhanced_image.save(buf, format="PNG")
    byte_im = buf.getvalue()

    st.download_button(
        label="Download Enhanced Image",
        data=byte_im,
        file_name="enhanced_image.png",
        mime="image/png"
    )
