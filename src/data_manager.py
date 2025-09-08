
try:
    from src.access_manager import AccessManager as am
except:
    from access_manager import AccessManager as am

class DataManager:
    def __init__(self):
        pass

    def create_table(self):
        query = f"CREATE TABLE products(name, price, cost)"
        res = am().execute_query(query)
        return res

    def add_products(self, products):
        query = "INSERT INTO products VALUES (?,?,?)"
        res = am().upload_many_query(query, products)
        return res

    def get_products(self):
        query = "SELECT * FROM products"
        res = am().execute_query(query)
        return res.fetchall()

    

