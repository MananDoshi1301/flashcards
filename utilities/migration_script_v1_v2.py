import os, json, uuid
import dbm.ndbm as ndbm
import dbm as sqlite3

def get_data_path(filename: str = None):
    base_path = os.getcwd()
    base_path = os.path.abspath(os.curdir)     
    data_dir_path = "data"
    path = os.path.join(base_path, data_dir_path)
    if filename: path = os.path.join(path, filename)
    return path

class MigrateToV2:    

    def __init__(self, old_filename, abs_path=None):                
        self.db_path = get_data_path(filename=old_filename)
        print(self.db_path)
        newfilename = f"{old_filename}_v2"
        self.new_db_path = get_data_path(filename=newfilename)
        print(self.new_db_path)
        
        if abs_path != None and abs_path != "":
            self.db_path = os.path.join(abs_path, old_filename)
            self.new_db_path = os.path.join(abs_path, newfilename)
            print("Opening Absolute paths!")
            
        self.db = sqlite3.open(self.db_path, 'r')
        self.new_db = ndbm.open(self.new_db_path, 'c')
        print("Both dbs opened!")
    
    def __del__(self):
        if self.db: self.db.close()
        if self.new_db: self.new_db.close()
    
    def __decode(self, item: bytes):
        return item.decode()

    # def __format_data(self, key, value):
    #     package = {
    #         "question": value["question"],
    #         "answer": value["answer"],
    #         "category": "None"
    #     }
    #     id = key
    #     return id, package

    # def migrate(self):
    #     for k in list(self.db.keys()):
    #         v = self.db[k]
    #         # Decode k, v
    #         key = self.__decode(k)
    #         value_json = self.__decode(v)
    #         value = json.loads(value_json)
    #         print(key, type(key), value, type(value))
    #         # Get data in format
    #         new_key, package = self.__format_data(key=key, value=value)

    #         # add to new db
    #         self.new_db[new_key] = json.dumps(package)  
    #     print()

    def __format_data(self, key, value):
        package = {
            "question": key,
            "answer": value,
            "category": "None"
        }
        id = str(uuid.uuid4())
        return id, package

    def migrate(self):
        for k in list(self.db.keys()):
            v = self.db[k]
            # Decode k, v
            key = self.__decode(k)
            value = self.__decode(v)
            # value = json.loads(value_json)
            print(key, type(key), value, type(value))
            # Get data in format
            new_key, package = self.__format_data(key=key, value=value)

            # add to new db
            self.new_db[new_key] = json.dumps(package)  
        print()
    
    def print_og_keys(self):
        for k in list(self.db.keys()):
            v = self.db[k]
            # Decode k, v
            key = self.__decode(k)
            value_json = self.__decode(v)
            print(key, value_json)

    def print_keys(self):

        for k in list(self.new_db.keys()):
            v = self.new_db[k]

            key = self.__decode(k)
            value_json = self.__decode(v)
            value = json.loads(value_json)
            print(key, value)



if __name__ == "__main__":
    # Run from root of directory    
    filename = "3_data"    
    abs_path = input("Absolute path: ")
    migrate_manager = MigrateToV2(old_filename=filename, abs_path=abs_path)
    migrate_manager.print_og_keys()
    migrate_manager.migrate()
    print("Printing keys")
    migrate_manager.print_keys()    
    # 3_data
    