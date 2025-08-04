import os


def get_files_info(working_directory, directory="."):
    # var for full path
    full_path = os.path.join(working_directory, directory)
    
    # var for absolute path
    abs_path = os.path.abspath(full_path)
    
    # var for absolute working directory
    abs_working_directory = os.path.abspath(working_directory)

    # var to build contents of the directory
    formatted_content_str = ""

    # try/except block to build str and catch errors if they arise
    try:
        # check to see if the directory is outside the working_directory
        if not abs_path.startswith(abs_working_directory):
            return f'    Error: Cannot list "{directory}" as it is outside the permitted working directory'
        
        # check to make sure the {directory} is a directory 
        if not os.path.isdir(abs_path):
            return f'    Error: "{directory}" is not a directory'
        
        # loop to build formated_content_str   
        for item_name in os.listdir(abs_path):
            full_item_path = os.path.join(abs_path, item_name)
            formatted_content_str += f' - {item_name}: file_size={os.path.getsize(full_item_path)} bytes, is_dir={os.path.isdir(full_item_path)}\n'
    except Exception as e:
        return f'Error: {e}'
    
    return formatted_content_str