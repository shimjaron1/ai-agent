import os
from dotenv import load_dotenv
from google import genai
import sys

def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    if len(sys.argv) < 2:
        sys.exit(1)
    user_input = " ".join(sys.argv[1:])
    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(model="gemini-2.0-flash-001", 
                                            contents=user_input)
    print(response.text)
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")


if __name__ == "__main__":
    main()