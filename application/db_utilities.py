import os 

def get_data_path(filename: str = None):
    base_path = os.getcwd()
    data_dir_path = "data"
    path = os.path.join(base_path, data_dir_path)
    if filename: path = os.path.join(path, filename)
    return path