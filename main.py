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



while True:
    print("\n=== МЕНЮ УПРАВЛЕНИЯ МАГАЗИНОМ ===")
    print("1. Посмотреть все товары")
    print("2. Добавить новый товар")
    print("3. Выйти из программы")
    
    choice = input("Выбери действие (1, 2 или 3): ")
    
    if choice == "1":
        # Вызываем нашу готовую функцию чтения
        show_all_products()
        
    elif choice == "2":
        # Собираем данные с клавиатуры
        print("\n--- Ввод данных нового товара ---")
        user_name = input("Введите название товара (например, Vinted Item): ")
        user_price = float(input("Введите цену (например, 45.50): "))
        user_category = input("Введите категорию (clothes/shoes/cosmetics): ")
        user_stock = int(input("Введите количество на складе: "))
        
        # Передаем собранные переменные в нашу функцию добавления!
        add_product(user_name, user_price, user_category, user_stock)
        
    elif choice == "3":
        print("До встречи! Программа завершена.")
        break  # Выходим из цикла
        
    else:
        print("Неверный выбор! Напиши цифру 1, 2 или 3.")