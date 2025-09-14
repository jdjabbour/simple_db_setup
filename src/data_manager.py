
from dataclasses import dataclass
from typing import List

# try:
#     from src.access_manager import AccessManager as am
# except:
#     from access_manager import AccessManager as am


# @dataclass
# class DataManager:
#     schema: dict
    

#     def create_table(self):
#         query = f"CREATE TABLE {self.table}{self.columns}"
#         res = am().execute_query(query)
#         return res

#     def add_items(self, items):
#         query = f"INSERT INTO {self.table} VALUES (?,?,?)"
#         res = am().upload_many_query(query, items)
#         return res

#     def get_items(self):
#         query = f"SELECT * FROM {self.table}"
#         res = am().execute_query(query)
#         return res.fetchall()

#     def add_items(self, items):
#         query = f"INSERT INTO {self.table} VALUES (?,?,?)"
#         res = am().upload_many_query(query, items)
#         return res
    


