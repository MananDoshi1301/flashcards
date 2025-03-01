import shelve
from application.db_utilities import get_data_path

class BaseDb:
    def __init__(self, filename):
        # print(filename)
        self.db = shelve.open(filename=get_data_path(filename))

    def __del__(self):
        if self.db:
            self.db.sync()
            self.db.close()