import os

# ✅ Set Hugging Face cache directories to D: drive
os.environ["HF_HOME"] = "D:/huggingface"
os.environ["TRANSFORMERS_CACHE"] = "D:/huggingface/transformers"
os.environ["HF_DATASETS_CACHE"] = "D:/huggingface/datasets"
os.environ["HF_METRICS_CACHE"] = "D:/huggingface/metrics"
os.environ["XDG_CACHE_HOME"] = "D:/huggingface"

# ✅ Import after setting environment variables
from transformers import pipeline

# ✅ Download TinyLlama (for logical tutor)
try:
    print("Downloading TinyLlama...")
    _ = pipeline("text-generation", model="TinyLlama/TinyLlama-1.1B-Chat-v1.0")
    print("✅ TinyLlama downloaded successfully.")
except Exception as e:
    print(f"❌ Failed to download TinyLlama: {e}")

print("🎯 Model downloading script completed.")
