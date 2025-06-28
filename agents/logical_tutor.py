import os
os.environ["HF_HOME"] = "D:/huggingface"
from transformers import pipeline
import os


from dotenv import load_dotenv

print("Initializing logical tutor...")  # Debug print

load_dotenv()

# Initialize the pipeline once to avoid reloading every call
try:
    print("Loading TinyLlama model...")  # Debug print
    generator = pipeline("text-generation", model="TinyLlama/TinyLlama-1.1B-Chat-v1.0")
    print("TinyLlama model loaded successfully")  # Debug print
except Exception as e:
    print(f"Error loading TinyLlama model: {e}")  # Debug print
    raise

def get_logical_explanation(topic):
    print(f"Generating explanation for topic: {topic}")  # Debug print
    prompt = (
        "You are a helpful educational tutor. Provide a concise explanation of the following topic:\n"
        f"Topic: {topic}\n\n"
        "Please structure your explanation with:\n"
        "- A brief introduction\n"
        "- Main concepts and principles\n"
        "- Step-by-step explanation\n"
        "- Real-world examples\n"
        "- Summary\n\n"
        "Explanation:"
    )
    try:
        print("Generating text...")  # Debug print
        result = generator(
            prompt,
            max_length=400,
            do_sample=True,
            temperature=0.7,
            top_p=0.9,
            repetition_penalty=1.2,
            truncation=True,
            pad_token_id=generator.tokenizer.eos_token_id
        )[0]['generated_text']
        
        print("Text generation completed")  # Debug print
        
        # Remove the prompt from the output
        if result.startswith(prompt):
            result = result[len(prompt):].strip()
        
        return result
    except Exception as e:
        print(f"Error in get_logical_explanation: {e}")  # Debug print
        return f"Error generating explanation: {e}"

def test_model_loading():
    print("Attempting to load model and generate text...")
    try:
        # Re-initialize pipeline for testing purposes within this function
        test_generator = pipeline("text-generation", model="TinyLlama/TinyLlama-1.1B-Chat-v1.0")
        test_prompt = "Generate a short sentence."
        test_result = test_generator(test_prompt, max_length=20, do_sample=False)[0]['generated_text']
        print(f"Model loaded successfully. Test generation output: {test_result}")
    except Exception as e:
        print(f"Error loading model or generating text: {e}")

if __name__ == "__main__":
    test_model_loading()
