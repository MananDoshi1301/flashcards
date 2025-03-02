import shelve, os
import dbm
from application.db_utilities import get_data_path

class BaseDb:
    def __init__(self, filename, flag='c'):
        
        self.db_path = get_data_path(filename=filename)
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)        
        self.db = dbm.open(self.db_path, 'c')

    def __del__(self):
        if self.db:
            # self.db.sync()
            self.db.close()