import bd
from random import choice

customers_ids = bd.get_customers_ids()
products_ids = bd.get_products_ids()

for i in range(1, 500):
    bd.add_order(choice(customers_ids), choice(products_ids))
