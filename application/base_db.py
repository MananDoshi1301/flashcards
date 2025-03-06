import shelve, os, dbm.sqlite3 as sqlite3, json
from typing import Any
from application.db_utilities import get_data_path

class BaseDb:
    def __init__(self, filename, flag='c'):
        
        self.db_path = get_data_path(filename=filename)
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)        
        self.db = sqlite3.open(self.db_path, 'c')

    def __del__(self):
        if self.db:
            # self.db.sync()
            self.db.close()

    def flush_data(self, key: str, value: dict) -> bool:
        try:
            self.db[key] = json.dumps(value) 
            return True
        except Exception as e:
            raise e
        return False              

    def get_data(self, object, json_load = False):
        decoded_object = object
        
        # Decoding bytes
        decoded_object = object.decode() if isinstance(object, bytes) else decoded_object
        
        # Decoding if json        
        decoded_object = json.loads(decoded_object) if json_load else decoded_object

        return decoded_object        