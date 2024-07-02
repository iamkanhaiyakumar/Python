# import os

# # Get the environment variables dictionary
# env_vars = os.environ

# # Print the contents of the environment variables dictionary
# for key, value in env_vars.items():
#     print(f'{key}: {value}')

import os
import time

def get_file_properties(directory):
    file_properties = {}
    
    # List all files in the given directory
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        
        # Check if it is a file (not a directory)
        if os.path.isfile(filepath):
            # Get file properties
            file_info = os.stat(filepath)
            file_properties[filename] = {
                'Size (in bytes)': file_info.st_size,
                'Creation Time': time.ctime(file_info.st_ctime),
                'Modification Time': time.ctime(file_info.st_mtime)
            }
    
    return file_properties

def print_file_properties(properties):
    for filename, props in properties.items():
        print(f'File: {filename}')
        for key, value in props.items():
            print(f'  {key}: {value}')
        print()

# Specify the directory to scan
directory_to_scan = '.'

# Get file properties for all files in the specified directory
file_properties = get_file_properties(directory_to_scan)

# Print the file properties
print_file_properties(file_properties)
