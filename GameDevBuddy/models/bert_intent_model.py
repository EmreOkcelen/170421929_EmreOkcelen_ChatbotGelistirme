# models/bert_intent_model.py

import torch
import pickle
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import os

# path ayarı: app.py ile aynı root içinde çalışacak şekilde
BERT_MODEL_PATH = os.path.join(os.path.dirname(__file__), "bert_intent_model")

class BertIntentModel:
    def __init__(self):
        self.model_name = BERT_MODEL_PATH
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

# Singleton
_bert_model = BertIntentModel()

def bert_intent_predict(text):
    return _bert_model.predict(text)
