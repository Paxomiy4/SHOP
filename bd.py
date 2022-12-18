import psycopg2
import config

try:
    # пытаемся подключиться к базе данных
    conn = psycopg2.connect(dbname='SHOP', user='postgres', password=config.password, host='localhost')
    print('connected')
except:
    # в случае сбоя подключения будет выведено сообщение в STDOUT
    print('Can`t establish connection to database')


def get_customers():
    with conn.cursor() as curs:
        curs.execute('SELECT * FROM customers')
        all_customers = curs.fetchall()
        return all_customers


def get_customer(customer_id):
    with conn.cursor() as curs:
        curs.execute('SELECT * FROM customers WHERE id=%s', (customer_id,))
        customer = curs.fetchone()
        return customer


def add_customer(name, address):
    with conn.cursor() as curs:
        curs.execute('INSERT INTO customers (name, address) values (%s, %s)', (name, address,))
        conn.commit()


def get_products():
    with conn.cursor() as curs:
        curs.execute('SELECT * FROM product')
        all_products = curs.fetchall()
        return all_products


def get_product(product_id):
    with conn.cursor() as curs:
        curs.execute('SELECT * FROM product WHERE id=%s', (product_id,))
        product = curs.fetchone()
        return product


def get_orders():
    with conn.cursor() as curs:
        curs.execute('SELECT * FROM orders')
        all_orders = curs.fetchall()
        return all_orders


def get_order(order_id):
    with conn.cursor() as curs:
        curs.execute('SELECT * FROM orders WHERE id=%s', (order_id,))
        order = curs.fetchone()
        return order


def get_customer_orders(customer_id):
    with conn.cursor() as curs:
        curs.execute('SELECT * FROM customers WHERE id=%s', (customer_id,))
        curs.execute('SELECT * FROM orders WHERE customer_id=%s', (customer_id,))
        orders = curs.fetchall()
        return orders


def get_product_orders(product_id):
    with conn.cursor() as curs:
        curs.execute('SELECT * FROM product WHERE id=%s', (product_id,))
        curs.execute('SELECT * FROM orders WHERE product_id=%s', (product_id,))
        orders = curs.fetchall()
        return orders


def add_order(customer_id, product_id):
    with conn.cursor() as curs:
        curs.execute('INSERT INTO orders (customer_id, product_id) values (%s, %s)', (customer_id, product_id,))
        conn.commit()
