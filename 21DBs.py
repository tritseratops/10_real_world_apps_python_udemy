import sqlite3

def create_table():
    conn = sqlite3.connect("lite.db")
    curs = conn.cursor()
    curs.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()

def insert_data(item, quantity, price):
    conn = sqlite3.connect("lite.db")
    curs = conn.cursor()
    curs.execute(f"INSERT INTO store values (?,?,?)", (item,quantity,price))
    conn.commit()
    conn.close()

# insert_data('Coffee Cup', 10, 6)

def view_data():
    conn = sqlite3.connect("lite.db")
    curs = conn.cursor()
    curs.execute("SELECT * FROM store")
    rows = curs.fetchall()
    for row in rows:
        print(row)
    conn.close()

def delete_data(item):
    conn = sqlite3.connect("lite.db")
    curs = conn.cursor()
    curs.execute("DELETE FROM store WHERE item=?", (item,))
    conn.commit()
    conn.close()

def update_data(item_to_update, new_name, new_qty, new_price):
    conn = sqlite3.connect("lite.db")
    curs = conn.cursor()
    curs.execute("UPDATE store SET item=?, quantity=?, price=? WHERE item=?", (new_name, new_qty, new_price, item_to_update))
    conn.commit()
    conn.close()

view_data()
# delete_data('Water Glass')
update_data('Coffee Cup', 'Coffe Mug', 30, 15)
view_data()