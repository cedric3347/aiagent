from google import genai
from google.genai import types
from functions.get_file_content import get_file_content
from functions.get_files_info import get_files_info
from functions.run_python import run_python_file
from functions.write_file import write_file



# map of function name to functions
function_map = {"get_file_content": get_file_content,
                "get_files_info": get_files_info,
                "run_python_file": run_python_file,
                "write_file": write_file,
                } 

# function that will handle calling functions
def call_function(function_call_part, verbose=False):
    # if verbose is specified
    if verbose:
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    
    else:
        print(f" - Calling function: {function_call_part.name}")

    # manually adds "working_directory" arg to function_call_part.args
    function_call_part.args["working_directory"] = "./calculator"      

    # calls function
    if function_call_part.name in function_map:
        try:
            function_result = function_map[function_call_part.name](**function_call_part.args)
            return types.Content(
                role="tool",
                parts=[
                    types.Part.from_function_response(
                        name=function_call_part.name,
                        response={"result": function_result},
                    )
                ],
            )
        
        # returns types.Content with a from_function_response describing the result of function call
        except TypeError as e:
            return types.Content(
                role="tool",
                parts=[
                    types.Part.from_function_response(
                        name=function_call_part.name,
                        response={"error": f"Function '{function_call_part.name}' encountered an error: {e}"},
                    )
                ],
            )
        
    # if function is name is invalid - returns a "types.Content" to explain error
    else:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_call_part.name,
                    response={"error": f"Unknown function: {function_call_part.name}"},
                )
            ],
        )