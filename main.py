import streamlit as st
from PIL import Image
import os

# Directory to store uploaded images
UPLOAD_DIR = 'uploaded_images'
if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)

def main():
    st.title("Image Search App")

    # Upload images
    uploaded_files = st.file_uploader("Upload Images", type=['png', 'jpg', 'jpeg'], accept_multiple_files=True)
    if uploaded_files:
        for file in uploaded_files:
            with open(os.path.join(UPLOAD_DIR, file.name), "wb") as f:
                f.write(file.getbuffer())
        st.success("Images uploaded successfully!")

    # Search for an image
    description = st.text_input("Enter Image Description:")
    if description:
        image_path = os.path.join(UPLOAD_DIR, description + ".jpg")
        if not os.path.isfile(image_path):
            image_path = os.path.join(UPLOAD_DIR, description + ".png")
        if not os.path.isfile(image_path):
            image_path = os.path.join(UPLOAD_DIR, description + ".jpeg")

        if os.path.isfile(image_path):
            img = Image.open(image_path)
            st.image(img, caption=f"Image: {description}")
        else:
            st.warning("Image not found.")

if __name__ == "__main__":
    main()
