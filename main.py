from tinydb import TinyDB

db = TinyDB('db.json')
products = open('products.csv').read().split('\n')
print(products)
for row in products:
    print(row)