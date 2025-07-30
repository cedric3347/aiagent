import os
import sys 
from dotenv import load_dotenv
from google import genai
from google.genai import types


def main():
    
    # sends prompt to Gemini API
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    # user prompt conversion
    prompt = ' '.join(sys.argv[1:])

    messages = [types.Content(role="user", parts=[types.Part(text=prompt)])]
    
    # check for sys.argv argument
    if len(sys.argv) > 1 :
        response = client.models.generate_content(model='gemini-2.0-flash-001', contents=messages)


        # checks for "--verbose" flag and prints more info about a prompt
        if sys.argv[-1] == "--verbose":
            split_prompt = prompt.split(' ')
            prompt_without_last = split_prompt[:-1]
            print(f'User prompt: "{' '.join(prompt_without_last)}"')
            print(f'Prompt tokens: {response.usage_metadata.prompt_token_count}')
            print(f'Response tokens: {response.usage_metadata.candidates_token_count}')


    # gives insturctions on how to use the program   
    else:
        print('This program requires a command-line argument...\n')
        print('Usage: \n python3 main.py <enter your prompt here> \n')
        print('For more information use the flag "--verbose" at the end of your prompt\n')
        print("No prompt detected...Exiting Program")
        sys.exit(1)

    # prints outputs
    print(f'Response:\n {response.text}')

if __name__== "__main__":
    main()