import os
os.environ.setdefault("HF_HUB_DOWNLOAD_TIMEOUT", "10")
os.environ.setdefault("HF_HUB_ETAG_TIMEOUT", "5")

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

# Load the model lazily so a failed/slow download doesn't crash the whole app.
explain_tokenizer = None
explain_model = None
_load_error = None


def _load_model():
    global explain_tokenizer, explain_model, _load_error
    if explain_model is not None or _load_error is not None:
        return
    try:
        explain_tokenizer = AutoTokenizer.from_pretrained("MBZUAI/LaMini-Flan-T5-783M")
        explain_model = AutoModelForSeq2SeqLM.from_pretrained("MBZUAI/LaMini-Flan-T5-783M")
    except Exception as e:
        _load_error = str(e)


def explain_topic(topic: str) -> str:
    _load_model()
    if _load_error:
        return f"Explanation model could not be loaded (network/download issue): {_load_error}"

    input_text = f"Explain the concept of '{topic}' in a simple and clear way for a school student."
    inputs = explain_tokenizer(input_text, return_tensors="pt")

    outputs = explain_model.generate(
        **inputs,
        max_new_tokens=150,
        temperature=0.7,
        top_k=50,
        top_p=0.95,
        do_sample=True
    )

    explanation = explain_tokenizer.decode(outputs[0], skip_special_tokens=True)
    return explanation
