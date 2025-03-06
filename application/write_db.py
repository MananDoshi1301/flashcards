import uuid, json
from typing import Any
from application.base_db import BaseDb

class DbWrite(BaseDb):            

    def __init__(self, *args, **kwargs):        
        super().__init__(*args, **kwargs)        

    def __del__(self):
        if self.db: self.db.close()
    
    def write_to_db(self, question: str, answer: Any, category: str = "None") -> bool:                
        id = str(uuid.uuid4()) 
        package = {
            "question": question,
            "answer": answer,
            "category": category
        }
        # package = [key, value, category]
        self.flush_data(id, package)               
        return True, id

    # Expects unique hash to delete from the table
    def delete_from_db(self, key: str) -> bool:
        if key in self.db:
            del self.db[key]
            return True
        return False
