# Image Search System Using CLIP

## Overview

This project is an image search system that allows users to search for images within a specified directory based on textual descriptions. The system utilizes OpenAI's CLIP (Contrastive Language–Image Pre-training) model to generate embeddings for both images and user input descriptions, enabling efficient similarity-based searches.

## How It Works

1. **Image Directory Selection:** The application prompts you to select a directory containing the images you want to search through.

2. **Text Description Generation:** Using the CLIP model, the project generates text descriptions (embeddings) for all the images in the chosen directory.

3. **Search Functionality:** When you enter a text description, the system converts it into an embedding using the CLIP model. It then calculates the cosine similarity between this embedding and the embeddings of the images to return the most relevant images matching your description.

4. **Vector Database Integration:** To optimize performance, the project includes a vector database that stores the precomputed embeddings of the images. This reduces both the computation cost and time required for the CLIP model to process the same images repeatedly.

## About CLIP

CLIP (Contrastive Language–Image Pre-training) is a model developed by OpenAI that connects textual descriptions with corresponding images. It achieves this by learning to predict which caption from a set of captions is most likely to match a given image. This is done through a contrastive learning approach where the model simultaneously learns to associate images with their matching text and differentiate them from non-matching text. CLIP uses a dual-encoder architecture: one encoder processes images, and the other processes text. The outputs are embeddings that can be directly compared using cosine similarity to find the most relevant matches between text and images.

## Getting Started

### Prerequisites

- Firebase.json has to be uploaded to the src folder
- .env also has to be uploaded to the project folder
- Required Python packages (see `requirements.txt`)

### Setup

1. **Clone the Repository:**

   ```Powershell
   git clone https://github.com/abudubai16/saras-ai-hackathon
   cd <project directory>

2. **Run Application**
   ```Powershell
   python run_project.py