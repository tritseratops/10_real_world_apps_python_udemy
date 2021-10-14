import psycopg2

def create_table():
    conn = psycopg2.connect("dbname='store21' user='postgres' password='in'  host='localhost' port='5432'")
    curs = conn.cursor()
    curs.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()

def insert_data(item, quantity, price):
    conn = psycopg2.connect("dbname='store21' user='postgres' password='postgressa'  host='localhost' port='5432'")
    curs = conn.cursor()
    curs.execute("INSERT INTO store values (%s,%s,%s)", (item,quantity,price))
    conn.commit()
    conn.close()

# insert_data('Coffee Cup', 10, 6)

def view_data():
    conn = psycopg2.connect("dbname='store21' user='postgres' password='postgressa'  host='localhost' port='5432'")
    curs = conn.cursor()
    curs.execute("SELECT * FROM store")
    rows = curs.fetchall()
    print("**************")
    for row in rows:
        print(row)
    conn.close()

def delete_data(item):
    conn = psycopg2.connect("dbname='store21' user='postgres' password='postgressa'  host='localhost' port='5432'")
    curs = conn.cursor()
    curs.execute("DELETE FROM store WHERE item=%s", (item,))
    conn.commit()
    conn.close()

def update_data(item_to_update, new_name, new_qty, new_price):
    conn = psycopg2.connect("dbname='store21' user='postgres' password='postgressa'  host='localhost' port='5432'")
    curs = conn.cursor()
    curs.execute("UPDATE store SET item=%s, quantity=%s, price=%s WHERE item=%s", (new_name, new_qty, new_price, item_to_update))
    conn.commit()
    conn.close()

create_table()
view_data()
insert_data('Wine Glass', 8, 50)
view_data()
# delete_data('Wine Glass')
update_data('Orange Glass', 'Apple Mug', 30, 15)
view_data()

# delete_data('Water Glass')
# update_data('Coffee Cup', 'Coffe Mug', 30, 15)
# view_data()