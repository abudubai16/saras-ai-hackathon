import os


# Local Files
from src.vectorization import generate_embeddings


# External Dependencies
from firebase_config import db


def store_embeddings_db(images_folder: str) -> None:
    # Reference to Firestore collection
    embeddings_ref = db.collection('image_embeddings')

    image_names = os.listdir(images_folder)
    embeddings_to_return = []

    for image_name in image_names:
        image_path = os.path.join(images_folder, image_name)

        # Reference to the document
        doc_ref = embeddings_ref.document(image_name)
        doc = doc_ref.get()

        if doc.exists:
            # If image exists, retrieve the embeddings
            embeddings_to_return.append((image_name, doc.to_dict()['embedding']))
        else:
            # If image doesn't exist, generate embeddings and store them
            embeddings = generate_embeddings(image_path)
            embeddings_to_return.append((image_name, embeddings))

            # Store the new image in Firestore
            embeddings_ref.document(image_name).set({
                'image_path': image_path,
                'embedding': embeddings.tolist()  # Convert to list for Firestore
            })

    return embeddings_to_return
