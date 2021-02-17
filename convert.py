from tinydb import TinyDB

def insert_db(data_csv):
    db.truncate()
    products_db = []
    for row in products[1:]:
        cat,company=row.split(',')[1:]
        products_db.append({'category':cat,'company':company})
    return products_db

db = TinyDB('db.json')
products = open('products.csv').read().split('\n')
data = open('products.csv')

products_db = insert_db(data)

db.insert_multiple(products_db)