import os


# Local files
from src.vector_database import store_embeddings_db
from src.utils import get_highest_similarity_image


# External Dependencies 
import streamlit as st


# Function to validate the directory path
def validate_path(path):
    """Check if the provided path is a valid directory."""
    return os.path.isdir(path)

# Function to simulate fetching images
def fetch_images(description, num_images):
    """Simulate fetching images based on a description."""
    return get_highest_similarity_image(text=description, top_n=num_images)

# Streamlit App
def main():
    # Initialize session state for interface control
    if "interface" not in st.session_state:
        st.session_state.interface = 1

    # Interface 1: Welcome and Path Input
    if st.session_state.interface == 1:
        st.title("Welcome to Our Project!!!")

        # Text input for the directory path
        directory_path = st.text_input("Enter a directory path:")

        # Validate the directory path
        if directory_path:
            if validate_path(directory_path):
                st.success("Valid path!")
                # Confirm button
                if st.button("Confirm"):

                    # Store the images if those images are not in the database
                    store_embeddings_db(images_folder=directory_path)
                    
                    st.session_state.valid_path = directory_path
                    st.session_state.interface = 2
            else:
                st.error("Invalid path. Please enter a valid directory path.")

    # Interface 2: Choose Action
    elif st.session_state.interface == 2:
        st.title("Directory Actions")

        st.write(f"Directory selected: {st.session_state.valid_path}")

        if st.button("Query Images"):
            st.session_state.interface = 3

        if st.button("Modify Images"):
            st.warning("This functionality has not yet been added.")

    # Interface 3: Query Images
    elif st.session_state.interface == 3:
        st.title("Query Images")

        # Text input for image description
        description = st.text_input("Description of images:")

        # Slider to select the number of images
        num_images = st.slider("Number of images to display:", 1, 10, 5)

        # Search button
        if st.button("Search"):
            if description:
                st.write(f"Showing {num_images} images for description: {description}")

                # Fetch images (simulated)
                images = fetch_images(description, num_images)

                # Display images in a grid
                cols = st.columns(3)
                for i, (img_url, _) in enumerate(images):
                    with cols[i % 3]:
                        st.image(img_url)
            else:
                st.error("Please enter a description before searching.")


if __name__ == "__main__":
    main()