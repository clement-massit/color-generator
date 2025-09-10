import numpy as np
import os
import json
from huggingface_hub import login
from sentence_transformers import SentenceTransformer, util


class Config:
    EMBEDDING_MODEL = "google/embeddinggemma-300m" 
    TOP_K = 5    
    TOKEN = os.getenv("TOKEN")
  

class PaletteGenerator:
    def __init__(self, config: Config, colors):
        self.config = config
        self.colors = colors
        self.embedding_model = self._load_model()
        self.color_embeddings = self.compute_embeddings_corpus()
        self.prompt = self.get_user_input()
        
        palette = self.generate_palette(self.prompt)
        for color in palette: 
            print(f"{self.colors[color['corpus_id']]['name']}: {self.colors[color['corpus_id']]['hex']}  {round(color['score'], 2)}")
    
    def _login_to_hf(self):
        if self.config.TOKEN:
            print("Logging into Hugging Face Hub...")
            login(token=self.config.TOKEN)
        else:
            print("TOKEN not found. Proceeding without login.")
            print("Note: This may fail if the model is gated.")
        
    def _load_model(self):
        print(f"Initializing embedding model: {self.config.EMBEDDING_MODEL}...")
        try:
            return SentenceTransformer(self.config.EMBEDDING_MODEL)
        except Exception as e:
            print(f"Error loading model: {e}")
            raise
    
    def compute_embeddings_corpus(self):
        
        color_texts = [
            f"{color['name']}, {color['description']}"
            for color in self.colors
        ]
        embeddings = self.embedding_model.encode(
            color_texts
        )
        print("Embeddings computed successfully.")
        return embeddings
    
    def generate_palette(self, text_prompt):
        embedding_prompt = self.embedding_model.encode(text_prompt)
        
        top_hits = util.semantic_search(
            embedding_prompt, self.color_embeddings, top_k=self.config.TOP_K
        )[0]
        
        return top_hits
    
        
        
    
        

    def get_user_input(self):
        prompt = input("Enter a prompt: ")
        return prompt
    
if __name__ == "__main__":
    
    def prepare_colors():
        with open('COLOR_DATA.json','r',encoding='utf-8') as f:
            colors = json.load(f)['colors']
        return colors
            
    generator = PaletteGenerator(config=Config(), colors=prepare_colors())
