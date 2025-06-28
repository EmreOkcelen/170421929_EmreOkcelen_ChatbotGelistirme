import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import numpy as np
import pickle
import os

ROBERTA_MODEL_PATH = os.path.join(os.path.dirname(__file__), "roberta_intent_model")

class RobertaIntentModel:
    def __init__(self):
        self.model_name = ROBERTA_MODEL_PATH
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name, local_files_only=True)
        self.model = AutoModelForSequenceClassification.from_pretrained(self.model_name, local_files_only=True).to(self.device)
        with open(os.path.join(self.model_name, "label_encoder.pkl"), 'rb') as f:
            self.le = pickle.load(f)
        self.model.eval()

    def predict(self, text):
        inputs = self.tokenizer(text, return_tensors='pt', truncation=True, padding=True, max_length=128).to(self.device)
        with torch.no_grad():
            outputs = self.model(**inputs)
        logits = outputs.logits
        pred = torch.argmax(logits, dim=1).cpu().item()
        return self.le.inverse_transform([pred])[0]

_roberta_model = RobertaIntentModel()

def roberta_intent_predict(text):
    return _roberta_model.predict(text)
