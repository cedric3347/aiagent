import os
import subprocess



def run_python_file(working_directory, file_path, args=[]):
       # var for full path
    full_path = os.path.join(working_directory, file_path)
    
    # var for absolute path
    abs_path = os.path.abspath(full_path)
    
    # var for absolute working directory
    abs_working_directory = os.path.abspath(working_directory)

    # var for directory name
    dir_name = os.path.dirname(abs_path)

    # builds list of commands to pass into 'subprocess'
    commands = ["python", file_path] + args



# try/except block to build str and catch errors if they arise
    try:
        # check to see if the file_path is outside the working_directory
        if not abs_path.startswith(abs_working_directory):
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        
        # return error if file_path doesn't exist 
        if not os.path.isfile(abs_path):
            return f'Error: File "{file_path}" not found.'
        
        # if file does not end with ".py"
        if not file_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file.'
        
        # builds the completed_process object
        results = subprocess.run(commands, timeout=30, capture_output=True, cwd=working_directory, text=True)
       
        # holds final return str
        output = []

        # check if no output is produced
        if not results.stdout.strip() and not results.stderr.strip():
            return "No output produced."
        
        # adds stdout to final str
        output.append(f'STDOUT: {results.stdout}')

        # adds stderr to final str
        output.append(f'STDERR: {results.stderr}')

        # adds this if process exits with non-zero code
        if results.returncode != 0:
            output.append(f'Process exited with code {results.returncode}')

        
        # final return
        return "\n".join(output)
    
    except Exception as e:
        return f"Error: executing Python file: {e}"
    