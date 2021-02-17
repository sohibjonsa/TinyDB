from tinydb import TinyDB, Query
db = TinyDB('db.json')

products = open('products.csv').read().split('\n')

products.pop(0)

for row in products:
    print(row)

# sm1 = {'ID': 1, 'category': 'smartphone', 'company': 'Samsung'}
# sm2 = {'ID': 2, 'category': 'smartphone', 'company': 'Apple'}
# sm3 = {'ID': 3, 'category': 'smartphone', 'company': 'Huawei'}
# sm4 = {'ID': 4, 'category': 'smartphone', 'company': 'Oppo'}
# sm5 = {'ID': 5, 'category': 'smartphone', 'company': 'Xiaomi'}



# db.insert(sm1)
# db.insert(sm2)
# db.insert(sm3)
# db.insert(sm4)
# db.insert(sm5)