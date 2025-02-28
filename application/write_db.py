from typing import Any
import shelve

class DbWrite:            

    def __init__(self, filename):
        # print(filename)
        self.db = shelve.open(filename=filename)

    def __del__(self):
        if self.db: self.db.close()
    
    def write_to_db(self, key: str, value: Any) -> bool:
        # if not self.db: raise 
        self.db[key] = value    
        return True        
