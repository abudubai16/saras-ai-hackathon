
import os

# Local Files 
from src.vectorization import generate_embeddings
from src.const import ADMIN_KEY

# External Dependencies 
import singlestoredb as s2


def store_embeddings_db(images_folder: str) -> None:
    # Create a connection to the database
    conn = s2.connect(ADMIN_KEY)

    with conn:
        with conn.cursor() as cur:
            # Create table if it doesn't exist
            cur.execute('''CREATE TABLE IF NOT EXISTS image_embeddings (
                            id INT AUTO_INCREMENT PRIMARY KEY,
                            image_name VARCHAR(255),
                            image_path VARCHAR(255),
                            embedding BLOB
                           )''')

            image_names = os.listdir(images_folder)
            new_images = []
            embeddings_to_return = []

            for image_name in image_names:
                image_path = os.path.join(images_folder, image_name)

                # Check if the image already exists in the database
                cur.execute("SELECT embedding FROM image_embeddings WHERE image_path = %s",
                            (image_path,))
                result = cur.fetchone()

                if result:
                    # If image exists, retrieve the embeddings
                    embeddings_to_return.append((image_name, result[0]))
                else:
                    # If image doesn't exist, generate embeddings and store them
                    embeddings = generate_embeddings(image_path)
                    embeddings_to_return.append((image_name, embeddings))
                    new_images.append((image_name, image_path, embeddings.tobytes()))

            # Insert new images into the database
            if new_images:
                cur.executemany(
                    """INSERT INTO image_embeddings (image_name, image_path, embedding)
                    VALUES (%s, %s, %s)
                    ON DUPLICATE KEY UPDATE embedding=VALUES(embedding)""",
                    new_images
                )
                conn.commit()

    return embeddings_to_return