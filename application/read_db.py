from application.base_db import BaseDb
from typing import Dict
import random

class DbRead(BaseDb):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get_cards(self) -> Dict:
        if not self.db: raise

        questions_list = list(self.db.keys())
        res = {key: self.db[key] for key in questions_list}
        random.shuffle(questions_list)

        package = {
            "questions": questions_list,
            "results": res
        }
        return package