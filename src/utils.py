
# Local Files
from src.vectorization import generate_embeddings, get_text_embedding
from src.const import ADMIN_KEY

# External Dependencies 
import numpy as np
import singlestoredb as s2


def normalize(vector: np.array) -> np.array:
    """Normalize the vector."""
    mean = vector.mean()
    std = vector.std()
    if std == 0:  # Avoid division by zero
        return vector - mean
    return (vector - mean) / std


def get_similarity_score(vector1: np.array, vector2: np.array) -> float:
    """Calculate cosine similarity between two vectors."""
    return np.dot(normalize(vector1), normalize(vector2))


def get_highest_similarity_image(text: str, top_n: int) -> list:
    """Retrieve the top N images with the highest similarity to the given text."""
    try:
        # Create a connection to the database
        with s2.connect(ADMIN_KEY) as conn:
            with conn.cursor() as cur:
                # Fetch all image paths and embeddings
                cur.execute('SELECT image_path, embedding FROM image_embeddings')
                image_embeddings = cur.fetchall()

    except Exception as e:
        print(f"Error connecting to database or fetching data: {e}")
        return []

    try:
        # Compute the text embedding
        text_embed = get_text_embedding(text)
        text_embed = normalize(text_embed)

        similarities = []
        for image_path, embedding in image_embeddings:
            image_embed = np.frombuffer(embedding, dtype=np.float32)
            image_embed = normalize(image_embed)
            similarity_score = get_similarity_score(text_embed, image_embed)
            similarities.append((image_path, similarity_score))

        # Sort and return top N results
        similarities.sort(key=lambda x: x[1], reverse=False)
        return similarities[:top_n]

    except Exception as e:
        print(f"Error processing embeddings or computing similarities: {e}")
        return []