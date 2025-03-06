import os 

def get_data_path(filename: str = None):
    base_path = os.getcwd()
    base_path = os.path.abspath(os.curdir)     
    data_dir_path = "data"
    path = os.path.join(base_path, data_dir_path)
    if filename: path = os.path.join(path, filename)
    return path