import sqlite3

def init_db():
    conn = sqlite3.connect('homework.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            price REAL DEFAULT 0.0,
            quantity INTEGER DEFAULT 0
        )
    ''')
    conn.commit()
    conn.close()

def create_product(title, price, quantity):
    conn = sqlite3.connect('homework.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO products (title, price, quantity) VALUES (?, ?, ?)', 
                   (title, price, quantity))
    conn.commit()
    conn.close()
    print(f"Товар '{title}' успешно добавлен.")

def read_all_products():
    conn = sqlite3.connect('homework.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM products')
    rows = cursor.fetchall()
    conn.close()
    return rows

def update_product_price(product_id, new_price):
    conn = sqlite3.connect('homework.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE products SET price = ? WHERE id = ?', (new_price, product_id))
    conn.commit()
    conn.close()
    print(f"Цена товара с ID {product_id} обновлена.")

def delete_product(product_id):
    conn = sqlite3.connect('homework.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM products WHERE id = ?', (product_id,))
    conn.commit()
    conn.close()
    print(f"Товар с ID {product_id} удален.")

if __name__ == "__main__":
    init_db()
    
    create_product("Меч Артура", 500.5, 1)
    create_product("Зелье маны", 15.0, 10)
    
    print("\nСписок товаров в базе:")
    for p in read_all_products():
        print(p)
        
    update_product_price(1, 450.0)
    
    delete_product(2)
    
    print("\nИтоговый список:")
    print(read_all_products())