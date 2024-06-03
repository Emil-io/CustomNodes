import os
import json

def create_meta_files(root_dir):
    """
    This method creates meta fields for a file based on the directory it is in.
    The meta values are stored in a seperate json file.
    The name of the json file is the same as for the original file, just when the following ending concatenated: ".meta.json"
    """
    for foldername, subfolders, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith('.pdf') or filename.endswith('.txt'):
                filepath = os.path.join(foldername, filename)
                meta_filepath = filepath + ".meta.json"
                folder_name = os.path.basename(foldername)
                metadata = {"folder": folder_name}
                # Check if the meta file already exists, if not, create it
                if not os.path.exists(meta_filepath):
                    with open(meta_filepath, 'w') as meta_file:
                        json.dump(metadata, meta_file, indent=4)

# Provide the root directory of your file system
root_directory = "/Users/emildeepset/Desktop/open_data_copy_small/Doctrine 040503"
create_meta_files(root_directory)