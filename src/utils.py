import os
import numpy as np
from firebase_config import db
from src.vectorization import get_text_embedding

# Get and check if the entered path is valid
def get_valid_path()->str:
    path = None
    while True:
            path = input('Enter the directory of images')
            if os.path.exists(path=path):
                break
    return path


# Normalize vector embeddings
def normalize(vector: np.array) -> np.array:
    mean = vector.mean()
    std = vector.std()
    if std == 0:  # Avoid division by zero
        return vector - mean
    return (vector - mean) / std


# Get cosine simiarlity score between two embedding vectors
def get_similarity_score(vector1: np.array, vector2: np.array) -> float:
    """Calculate cosine similarity between two vectors."""
    return np.dot(normalize(vector1), normalize(vector2))


def get_highest_similarity_image(text: str, top_n: int) -> list:
    """Retrieve the top N images with the highest similarity to the given text."""
    try:
        # Reference to Firestore collection
        embeddings_ref = db.collection('image_embeddings')
        image_embeddings = [doc.to_dict() for doc in embeddings_ref.stream()]
    except Exception as e:
        print(f"Error connecting to Firestore or fetching data: {e}")
        return []

    try:
        # Compute the text embedding
        text_embed = get_text_embedding(text)
        text_embed = normalize(text_embed)

        similarities = []
        for doc in image_embeddings:
            image_path = doc['image_path']
            image_embed = np.array(doc['embedding'], dtype=np.float32)
            image_embed = normalize(image_embed)
            similarity_score = get_similarity_score(text_embed, image_embed)
            similarities.append((image_path, similarity_score))

        # Sort and return top N results
        similarities.sort(key=lambda x: x[1], reverse=True)
        return similarities[:top_n]

    except Exception as e:
        print(f"Error processing embeddings or computing similarities: {e}")
        return []
