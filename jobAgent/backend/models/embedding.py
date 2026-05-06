from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2") # pre-trained model that's lightweight for ecoding text into numerical vectors

def encode(text):
    return model.encode(text)