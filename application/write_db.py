import shelve
from typing import Any
from application.base_db import BaseDb

class DbWrite(BaseDb):            

    def __init__(self, *args, **kwargs):        
        super().__init__(*args, **kwargs)        

    def __del__(self):
        if self.db: self.db.close()
    
    def write_to_db(self, key: str, value: Any) -> bool:
        # if not self.db: raise 
        self.db[key] = value    
        return True 

    def delete_from_db(self, key: str) -> bool:
        if key in self.db:
            del self.db[key]
            return True
        return False
