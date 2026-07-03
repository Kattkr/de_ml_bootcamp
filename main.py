import psycopg2
def get_connection():
    return psycopg2.connect(
        host='localhost',
        port="5432",
        database='postgres',
        user="postgres",
        password="my_secret_pass"
    )
def add_product(name, price, category, stock):
    try:
        connection=get_connection()
        cursor=connection.cursor()
        sql=f"""
        INSERT INTO products (name, price, category, stock) 
        VALUES ('{name}', {price}, '{category}', {stock});
        """
        cursor.execute(sql)
        connection.commit()
        print(f"Ура! Товар '{name}' успешно добавлен!")
        cursor.close()
        connection.close()
    except Exception as error:
        print(f"Ошибка при добавлении: {error}")
def show_all_products():
    try:
        connection=get_connection()
        cursor=connection.cursor()
        cursor.execute("SELECT * FROM products;")
        all_products=cursor.fetchall()
        print("--- НАШИ ТОВАРЫ ИЗ БАЗЫ ДАННЫХ ---")
        for product in all_products:
            print(product)
        print("----------------------------------")
        
        cursor.close()
        connection.close()
    except Exception as error:
        print(f"Ошибка при чтении: {error}")
show_all_products()
#add_product('Sneakers Pacific Republic', 149.99, 'shoes', 3)
show_all_products()