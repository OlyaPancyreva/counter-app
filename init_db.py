import os
import psycopg2

# подключаемся к бд
def get_db_connection():
    conn = psycopg2.connect(host='localhost',
                            database='flask_db',
                            user=os.environ['DB_USERNAME'],
                            password=os.environ['DB_PASSWORD'])
    return conn


# получаем количество строк в таблице
def get_counter():
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute('CREATE TABLE if NOT EXISTS table_counter (id serial PRIMARY KEY,'
                'datetime varchar NOT NULL,'
                'client_info varchar NOT NULL);'
                )
    cur.execute('SELECT COUNT(*) FROM table_counter')
    count = cur.fetchone()[0]

    conn.commit()
    cur.close()
    conn.close()

    return count


# отправляем данные в таблицу
def set_counter(datetime, client_info):
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute('CREATE TABLE if NOT EXISTS table_counter (id serial PRIMARY KEY,'
                'datetime varchar NOT NULL,'
                'client_info varchar NOT NULL);'
                )

    cur.execute('INSERT INTO table_counter (datetime, client_info)'
                'VALUES (%s, %s)',
                (datetime, client_info))

    cur.execute('SELECT COUNT(*) FROM table_counter')
    count = cur.fetchone()[0]

    conn.commit()
    cur.close()
    conn.close()

    return count


# получаем всю таблицу полностью
def get_table():
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute('CREATE TABLE if NOT EXISTS table_counter (id serial PRIMARY KEY,'
                'datetime varchar NOT NULL,'
                'client_info varchar NOT NULL);'
                )

    cur.execute('SELECT * FROM table_counter')
    data = cur.fetchall()

    conn.commit()
    cur.close()
    conn.close()

    return data
