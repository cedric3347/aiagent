import os
import sys 
from dotenv import load_dotenv
from  google import genai
from google.genai import types


def main():
    
    # sends prompt to Gemini API
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    # user prompt conversion
    prompt = ' '.join(sys.argv[1:])

    messages = [types.Content(role="user", parts=[types.Part(text=prompt)])]
    
    #check for sys.argv argument
    if len(sys.argv) > 1 :
        response = client.models.generate_content(model='gemini-2.0-flash-001', contents=messages)

    # gives insturctions on how to use program   
    else:
        print('This program requires a command-line argument')
        print('Usage: python3 main.py <enter your prompt here>')
        print("No prompt detected...Exiting Program")
        sys.exit(1)

    # prints outputs
    print(f'Prompt tokens: {response.usage_metadata.prompt_token_count}')
    print(f'Response tokens: {response.usage_metadata.candidates_token_count}')
    print(f'Response:\n {response.text}')

if __name__== "__main__":
    main()