
import sqlite3
from connection_manager import ConnectionManager as CM

class AccessManager:
    def __init__(self):
        self.cur = CM().connect()  


    def execute_query(self, query: str) -> object:
        try:
            res = self.cur.execute(query)
            return res
        except Exception as e:
            print(f"!!! UPLOAD ERROR: {e} !!!")
            return 0

    def upload_many_query(self, query: str, params: list):
        try:
            self.cur.executemany(query, params)
            self.conn.commit()  
            return 1
        except Exception as e:
            print(f"!!! UPLOAD ERROR: {e} !!!")
            return 0
