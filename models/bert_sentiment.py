from transformers import BertTokenizer, BertForSequenceClassification
import torch
import json

tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertForSequenceClassification.from_pretrained('bert-base-uncased')

def analyze_news(news):
    text = news['title']
    inputs = tokenizer(text, return_tensors='pt', truncation=True, padding=True, max_length=512)
    outputs = model(**inputs)
    scores = outputs[0][0].detach().numpy()
    news['sentiment'] = scores
    return news
