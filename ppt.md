---
marp: true
theme: gaia
paginate: true
backgroundColor: #fff
color: #000
header: "Clash of T-AI-TANS"
footer: "Lil James @ Saras AI Institute"
---

# Clash of T-AI-TANS
**Advanced Image Retrieval System**  
**Presented by:**  
Lil James @ Saras AI Institute

---

## Introduction

### Objective:
- Develop an advanced image retrieval system that enables users to search for images based on textual descriptions.

### System Overview:
- Uses pre-trained models to understand and match the content of images with user-provided descriptions.

---

## Real-Life Applications (1/2)

### 1. Education:
- **Problem:** Difficulty in indexing and searching images in class notes.
- **Solution:** Text-based search for students to easily find images related to specific topics.

---

## Real-Life Applications (2/2)

### 2. Satellite Imaging:
- **Problem:** Challenges in identifying key features in vast satellite images.
- **Solution:** Search for events like landslides or tsunami survivors using descriptive text.

---

## High-Level Implementation (1/2)

### 1. Image Captioning Model:
- Uses pre-trained models (e.g., Git-Large by Microsoft) to generate text descriptions for images.

### 2. Text Embedding Model:
- Utilizes a model like BERT to convert descriptions into vectors, allowing similarity search through cosine similarity.

---

## High-Level Implementation (2/2)

### 3. Vector Database:
- Stores embedding vectors to reduce computational load and hardware requirements for queries.
