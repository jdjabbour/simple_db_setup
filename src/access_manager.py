
import sqlite3

class AccessManager:
    def __init__(self):
        self.conn = None
        self.cur = None  

    def execute_query(self, query: str) -> object:
        self.create_conn()
        self.create_cur()

        try:
            res = self.cur.execute(query)
            return res
        except Exception as e:
            print(f"!!! UPLOAD ERROR: {e} !!!")
            return 0


    def upload_many_query(self, query: str, params: list):
        self.create_conn()
        self.create_cur()

        try:
            self.cur.executemany(query, params)
            self.conn.commit()  
            return 1
        except Exception as e:
            print(f"!!! UPLOAD ERROR: {e} !!!")
            return 0




    def create_conn(self):
        self.conn = sqlite3.connect('products.db')

    def create_cur(self):
        self.cur = self.conn.cursor()

    def close_connection(self):
        self.conn.close()