import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import sys

def main():
    load_dotenv()
    # API Key input
    api_key = os.environ.get("GEMINI_API_KEY")

    # Validate input for call
    if len(sys.argv) < 2:
        sys.exit(1)

    # Tracking user prompt
    user_prompt = " ".join(sys.argv[1:])
    messages = [types.Content(role="user", parts=[types.Part(text=user_prompt)]),]

    # Call client and provide prompt
    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages)
    
    # If verbose
    if "--verbose" in sys.argv:
        print(response.text)
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

    else:
        print(response.text)

if __name__ == "__main__":
    main()