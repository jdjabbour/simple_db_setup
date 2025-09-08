
from dataclasses import dataclass
from typing import List
import sqlite3

@dataclass
class ConnectionManager:

    conn: object = None
    cur: object = None  

    def create_conn(self: object) -> object:
        try:
            self.conn = sqlite3.connect('products.db')
            return self.conn
        except Exception as e:
            print(f"!! ERROR CREATING CONNECTION !!")
            return 0
             
    def create_cur(self):
        try:
            self.cur = self.conn.cursor()
            return self.cur
        except Exception as e:
            print(f"!! ERROR CREATING CURSOR !!")
            return 0 

    def close_connection(self):
        try:
            self.conn.close()
            return 1
        except Exception as e:
            print(f"!! ERROR CREATING CURSOR !!")
            return 0