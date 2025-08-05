import os



def write_file(working_directory, file_path, content):
       # var for full path
    full_path = os.path.join(working_directory, file_path)
    
    # var for absolute path
    abs_path = os.path.abspath(full_path)
    
    # var for absolute working directory
    abs_working_directory = os.path.abspath(working_directory)

    # var for directory name
    dir_name = os.path.dirname(abs_path)



# try/except block to build str and catch errors if they arise
    try:
        # check to see if the file_path is outside the working_directory
        if not abs_path.startswith(abs_working_directory):
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        
        # creates file_path if it doesn't exist 
        if not os.path.exists(dir_name):
            os.makedirs(dir_name)   
 
    except Exception as e:
        return f'Error: {e}'
    
    # overwrites file with what's in the 'content' argument
    with open(abs_path, "w") as f:
        f.write(content)

    # returns a success string so that the LLM knows that the action it took actually worked
    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'