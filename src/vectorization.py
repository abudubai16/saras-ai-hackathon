# Loccal files
from src.const import DEVICE


# External Dependencies
import torch 
from PIL import Image
from sentence_transformers import SentenceTransformer
from transformers import CLIPTokenizer, CLIPTextModel


def generate_embeddings(image_path):
    """Generate embeddings for a given image."""
    img_model = SentenceTransformer('clip-ViT-B-32', device=DEVICE)
    image = Image.open(image_path)
    return img_model.encode([image], show_progress_bar=False, device=DEVICE)[0]


def get_text_embedding(text):

  model_name = 'openai/clip-vit-base-patch32'
  tokenizer = CLIPTokenizer.from_pretrained(model_name)
  model = CLIPTextModel.from_pretrained(model_name)

  """Generate an embedding for the given text."""
  inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True)
  with torch.no_grad():
      outputs = model(**inputs)
  # Extract the last hidden state
  embedding = outputs.last_hidden_state.mean(dim=1).cpu().numpy()

  del tokenizer
  del model

  return embedding