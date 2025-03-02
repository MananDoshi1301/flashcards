import shelve, os
import dbm
from application.db_utilities import get_data_path

class BaseDb:
    def __init__(self, filename, flag='c'):
        # print(filename)
        # self.db_path = get_data_path(filename)
        # os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
        # self.db = shelve.open(self.db_path, flag=flag)
        # try:
        #     self.db = shelve.open(self.db_path, flag=flag)
        # except Exception as e:
        #     print(f"Error opening shelve DB at {self.db_path}: {e}")
        #     self.db = None  # Prevent further access issues

        self.db_path = get_data_path(filename=filename)
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
        print("Opening File in Parent")
        self.db = dbm.open(self.db_path, 'c')

    def __del__(self):
        if self.db:
            # self.db.sync()
            self.db.close()