
import os

# External Dependencies 
import torch
from dotenv import load_dotenv

load_dotenv()

DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
PATH = os.getcwd()
ADMIN_KEY = os.getenv('ADMIN_KEY')