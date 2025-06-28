import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# Initialize Groq client
client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

def get_quiz_questions(topic):
    try:
        print(f"Generating quiz for topic: {topic}")

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": "You are a helpful quiz generator. Generate clear, educational multiple-choice questions."},
                {
                    "role": "user",
                    "content": (
                        f"Generate 3 multiple-choice quiz questions on the topic '{topic}'. "
                        "Each question should have 4 options (A, B, C, D) and clearly mark the correct answer. "
                        "Format each question with a number, followed by the question text, then options A through D, "
                        "and finally indicate the correct answer."
                    )
                }
            ],
            temperature=0.7,
            max_tokens=500
        )

        output = response.choices[0].message.content
        print("\nModel Output:\n", output)
        return output

    except Exception as e:
        print(f"[ERROR] Quiz generation failed: {e}")
        return f"Error generating quiz questions: {e}"
