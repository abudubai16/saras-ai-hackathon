# Local Files
from src.utils import get_highest_similarity_image


def run_CLI():
    # Take input from the user
    user_text = input("Enter the text to find similar images: ")
    top_n = int(input("Enter the number of top similar images to retrieve: "))

    # Call the function to get top N similar images
    similar_images = get_highest_similarity_image(user_text, top_n)

    # Display the results
    if similar_images:
        print(f"\nTop {top_n} images most similar to '{user_text}':")
        for idx, (image_path, score) in enumerate(similar_images, 1):
            print(f"{idx}. {image_path} - Similarity Score: {score}")
    else:
        print("No similar images found or an error occurred.")


def run_gui():
    pass


if __name__ == "__main__":
    run_CLI()
    pass