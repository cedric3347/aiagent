import os
from config import MAX_CHARS



def get_file_content(working_directory, file_path):
        # var for full path
    full_path = os.path.join(working_directory, file_path)
    
    # var for absolute path
    abs_path = os.path.abspath(full_path)
    
    # var for absolute working directory
    abs_working_directory = os.path.abspath(working_directory)



# try/except block to build str and catch errors if they arise
    try:
        # check to see if the file_path is outside the working_directory
        if not abs_path.startswith(abs_working_directory):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        
        # check to make sure the {file_path} is a file 
        if not os.path.isfile(abs_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        
        # read file and return as string -> {formated_content_str}   
        with open(abs_path, "r") as f:
            file_content_str = f.read(MAX_CHARS)

            # check for file truncation by trying to read 1 more char and adding message to the end if needed
            if f.read(1):
                file_content_str += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
        
    except Exception as e:
        return f'Error: {e}'
    
    return file_content_str




