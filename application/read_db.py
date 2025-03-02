from application.base_db import BaseDb
from typing import Dict
import random

class DbRead(BaseDb):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get_cards(self) -> Dict:        
        questions_list = [key.decode() if isinstance(key, bytes) else key for key in self.db.keys()]        
        res = {key: self.db[key].decode() if isinstance(self.db[key], bytes) else self.db[key]  for key in questions_list}
        random.shuffle(questions_list)

        package = {
            "questions": questions_list,
            "results": res
        }
        return package