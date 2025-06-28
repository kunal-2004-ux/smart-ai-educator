import os
import sys
from dotenv import load_dotenv
from orchestrator import route_to_agent

print("Starting program...")  # Immediate debug print

# Load environment variables
print("Loading environment variables...")  # Debug print
load_dotenv()

def check_api_keys():
    print("Checking API keys...")  # Debug print
    required_keys = {
        "TOGETHER_API_KEY": "Story Tutor (Together API)",
        "GROQ_API_KEY": "Quiz Tutor (Groq API)",
        "GOOGLE_API_KEY": "Visual Tutor (Gemini API)"
    }
    
    missing_keys = [key for key, name in required_keys.items() if not os.getenv(key)]
    if missing_keys:
        print("\n⚠️ Error: Missing API Keys!")
        print("Please add the following API keys to your .env file:")
        for key in missing_keys:
            print(f"- {key} (for {required_keys[key]})")
        return False
    print("All API keys are present.")  # Debug print
    return True

def main():
    try:
        print("\n\U0001F4D8 Welcome to the Education Tutor!")
        print("Initializing...")
        
        # Check API keys first
        if not check_api_keys():
            print("Exiting due to missing API keys.")
            return
        
        print("\nSystem is ready!")
        
        while True:
            try:
                topic = input("\nEnter a topic you want to learn about (or 'quit' to exit): ")
                if topic.lower() == 'quit':
                    print("\nThank you for using the Education Tutor! Goodbye!")
                    break
                    
                print("\nAvailable learning styles:")
                print("1. logical - Step-by-step explanations")
                print("2. visual - Visual analogies and diagrams")
                print("3. story - Learning through stories")
                print("4. quiz - Test your knowledge")
                
                style = input("\nChoose your learning style (logical/visual/story/quiz): ").lower()
                
                if style not in ['logical', 'visual', 'story', 'quiz']:
                    print("\n⚠️ Invalid style! Please choose from: logical, visual, story, quiz")
                    continue
                
                print("\n\U0001F393 Generating your tailored learning output...\n")
                result = route_to_agent(topic, style)
                print("\n" + "="*50)
                print(result)
                print("="*50)
                
            except Exception as e:
                print(f"\n⚠️ An error occurred: {str(e)}")
                print("Please check your API keys and internet connection.")
                break
    except Exception as e:
        print(f"\n⚠️ Fatal error: {str(e)}")
        print("The program encountered an unexpected error.")
        print(f"Error type: {type(e).__name__}")  # Print error type
        import traceback
        print("Full error traceback:")
        traceback.print_exc()

if __name__ == "__main__":
    print("Program entry point reached")  # Debug print
    try:
        main()
    except Exception as e:
        print(f"Critical error in main: {e}")
        import traceback
        traceback.print_exc()