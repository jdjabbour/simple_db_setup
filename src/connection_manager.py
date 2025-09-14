
from dataclasses import dataclass
from typing import List
import sqlite3

@dataclass
class ConnectionManager:
    """_summary_
    This module is for managing the connection and cursor to the 
    db.

    Returns:
        _type_: _description_
    """
    db_name: str
    conn: object = None
    cur: object = None  

    def connect(self: object) -> sqlite3.Cursor:
        self.create_db_connection()
        self.create_cursor(self.conn)
        if self.cur:
            return self.cur



    def create_db_connection(self: object, table: str = 'products'):
        try:
            table = f"{table}.db"
            self.conn = sqlite3.connect(table)
            return self.conn
        except Exception as e:
            print(f"!! ERROR CREATING CONNECTION !!")
            return 0
             
    def create_db_cursor(self, conn):
        try:
            self.cur = conn.cursor()
            return self.cur
        except Exception as e:
            print(f"!! ERROR CREATING CURSOR !!")
            return 0 

    def close_db_connection(self):
        try:
            self.conn.close()
            return 1
        except Exception as e:
            print(f"!! ERROR CREATING CURSOR !!")
            return 0