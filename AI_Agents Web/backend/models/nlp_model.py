# backend/models/nlp_model.py
from transformers import pipeline

qa_pipeline = pipeline("question-answering")

def answer_query(query, context):
    result = qa_pipeline(question=query, context=context)
    return result["answer"]
