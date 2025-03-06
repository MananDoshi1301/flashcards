import os, shutil
from datetime import datetime

def create_directory():
    dir_path = os.getcwd()
    dir_name: str = "backups"
    dir = os.path.join(dir_path, dir_name)
    # Create directory if it does not exist
    os.makedirs(dir, exist_ok=True)    
    return dir    

def create_subdirectory(base_dir: str):
    
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    subdir_name = f"dir_{timestamp}"
    dir = os.path.join(base_dir, subdir_name)
    os.makedirs(dir, exist_ok=True)        
    return dir

def backup_files(source_path: str, destination_path: str):
    os.makedirs(destination_path, exist_ok=True)
    files = os.listdir(source_path)
    
    for file in files:
        src_path = os.path.join(source_path, file)
        dest_path = os.path.join(destination_path, file)
        
        if os.path.isfile(src_path):  # Ensure it's a file
            shutil.copy2(src_path, dest_path)
    
    print(f"Replicated {len(files)} files from {source_path} to {destination_path}")



if __name__ == "__main__":
    base_dir:str = create_directory()
    destination_path:str = create_subdirectory(base_dir)

    source_dir = os.path.join(os.getcwd(), "data")
    backup_files(source_dir, destination_path)