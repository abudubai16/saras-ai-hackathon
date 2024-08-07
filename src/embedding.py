from PIL import Image
from transformers import CLIPProcessor, CLIPModel
import torch
import pymysql
import os
import numpy as np

# Load the CLIP model and processor
model_name = 'openai/clip-vit-base-patch32'
model = CLIPModel.from_pretrained(model_name)
processor = CLIPProcessor.from_pretrained(model_name)

db_config = {
    'host': 'svc-ae8c5252-2f14-4cbf-a2e4-f0531b543234-dml.aws-oregon-3.svc.singlestore.com',
    'user': 'admin',
    'password': 'diyphEdVmqEFcydtlDBHPicUNkAoJ0MT',
    'database': 'sarasaidatabase',
    'port': 3306
}

def preprocess_image(image_path):
    """Load and preprocess an image."""
    image = Image.open(image_path).convert('RGB')
    return image

def generate_image_embedding(image):
    """Generate an embedding for the given image."""
    inputs = processor(images=image, return_tensors="pt")
    with torch.no_grad():
        outputs = model.get_image_features(**inputs)
    return outputs

def store_embedding(cursor, image_path, embedding):
    """Store the image path and embedding in the database."""
    embedding_np = embedding.cpu().detach().numpy()
    embedding_bytes = embedding_np.tobytes()
    
    sql = "INSERT INTO image_embeddings (image_path, embedding) VALUES (%s, %s)"
    cursor.execute(sql, (image_path, embedding_bytes))

def process_images(image_folder):
    """Process all images in the given folder."""
    connection = None
    cursor = None
    try:
        connection = pymysql.connect(**db_config)
        cursor = connection.cursor()

        cursor.execute("SELECT VERSION()")
        version = cursor.fetchone()
        print(f"Database version: {version[0]}")

        for filename in os.listdir(image_folder):
            if filename.lower().endswith(('png', 'jpg', 'jpeg')):
                image_path = os.path.join(image_folder, filename)
                image = preprocess_image(image_path)
                image_embedding = generate_image_embedding(image)
                store_embedding(cursor, image_path, image_embedding)
                print(f"Processed and stored embedding for {filename}")

        connection.commit()
    
    except pymysql.MySQLError as e:
        print(f"Database error: {e}")
    
    finally:
        if cursor:
            cursor.close()
        if connection and connection.open:
            connection.close()

# Specify the folder containing your images
image_folder = '/content/images'
process_images(image_folder)

def fetch_and_print_embeddings():
    """Fetch and print image embeddings from the database."""
    connection = None
    cursor = None
    try:
        connection = pymysql.connect(**db_config)
        cursor = connection.cursor()

        cursor.execute("SELECT image_path, embedding FROM image_embeddings")
        rows = cursor.fetchall()

        for row in rows:
            image_path = row[0]
            embedding_bytes = row[1]
            
            # Convert bytes back to NumPy array
            embedding_np = np.frombuffer(embedding_bytes, dtype=np.float32)
            
            # Print the image path and the embedding
            print(f"Image Path: {image_path}")
            print(f"Embedding: {embedding_np}")
            print()

    except pymysql.MySQLError as e:
        print(f"Database error: {e}")
    
    finally:
        if cursor:
            cursor.close()
        if connection and connection.open:
            connection.close()

# Call the function to fetch and print embeddings
fetch_and_print_embeddings()