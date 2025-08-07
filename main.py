import os
import sys 
from dotenv import load_dotenv
from google import genai
from google.genai import types
from config import system_prompt
from schemas.schema_get_files_info import schema_get_files_info
from config import available_functions
from functions.call_function import call_function
from config import iteration_max



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
        
        iterations = 0
        
        while True:
            if iterations >= iteration_max:
                sys.exit(f'The maximum amount of iterations has been reached ({iteration_max}).')
            
            response = client.models.generate_content(
                model='gemini-2.0-flash-001',
                contents=messages,
                config=types.GenerateContentConfig(
                    # sets tone for the conversation
                    system_instruction=system_prompt,
                    # function declaration
                    tools=[available_functions]),
            )

            # adds LLM's response to conversation
            for candidate in response.candidates:
                messages.append(candidate.content)

            # var for "--verbose" check
            verbose_flag = "--verbose" in sys.argv

            # uses the "call_function" function
            if response.function_calls:
                for function_call in response.function_calls:
                    function_call_result = call_function(function_call, verbose=verbose_flag)
                    
                    # add results immediately to the conversation
                    messages.append(function_call_result)
                
                    # checks for .parts[0].function_response.response
                    if not function_call_result.parts[0].function_response.response:
                        raise ValueError("Fatal error detected, unable to continue")

                    # verbose check
                    if verbose_flag:
                        print(f"-> {function_call_result.parts[0].function_response.response}")
                
            # checks for text response and final print and break after all function calls and LLM is done 
            else: 
                if response.text and response.text.strip():
                    print("Final response:")
                    print(response.text)
                    break

                else:
                    break
            

            # checks for "--verbose" flag and prints more info about a prompt
            if sys.argv[-1] == "--verbose":
                split_prompt = prompt.split(' ')
                prompt_without_last = split_prompt[:-1]
                print(f'User prompt: "{' '.join(prompt_without_last)}"')
                print(f'Prompt tokens: {response.usage_metadata.prompt_token_count}')
                print(f'Response tokens: {response.usage_metadata.candidates_token_count}')
            
            iterations += 1

    # gives insturctions on how to use the program   
    else:
        print('This program requires a command-line argument...\n')
        print('Usage: \n python3 main.py <enter your prompt here> \n')
        print('For more information use the flag "--verbose" at the end of your prompt\n')
        print("No prompt detected...Exiting Program")
        sys.exit(1)

    
if __name__== "__main__":
    main()