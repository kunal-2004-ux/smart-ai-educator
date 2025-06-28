import google.generativeai as genai
import os


from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")

def get_visual_explanation(topic):
    prompt = (
        f"Explain the following concept using visual metaphors, analogies, "
        f"and textual diagrams:\n\n{topic}"
    )
    response = model.generate_content(prompt)
    return response.text 