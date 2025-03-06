from application.base_db import BaseDb
from typing import Dict, List
import random, json

class DbRead(BaseDb):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    # def get_cards(self) -> Dict:        
    #     questions_list = [key.decode() if isinstance(key, bytes) else key for key in self.db.keys()]        
    #     res = {key: self.db[key].decode() if isinstance(self.db[key], bytes) else self.db[key]  for key in questions_list}
    #     random.shuffle(questions_list)

    #     package = {
    #         "questions": questions_list,
    #         "results": res
    #     }
    #     return package        

    def get_cards(self) -> Dict[str, Dict[str, dict] | List[str]]:
                
        categories = set()
        data = {}
        for k, v in self.db.items():
            id: str = self.get_data(k)            
            package: dict = self.get_data(v, json_load = True)            
            data[id] = package
            categories.add(package["category"])

        package = {            
            "data": data,
            "categories": list(categories)
        }
        return package    