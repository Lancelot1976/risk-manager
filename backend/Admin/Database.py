import sqlite3

class Database:
    _instance = None

    def __new__(cls, db_name="user.db"):
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls)
            cls._instance.connection = sqlite3.connect(db_name, check_same_thread=False)
        return cls._instance

    def get_connection(self):
        return self.connection
    
