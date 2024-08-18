import pymysql

def connect_to_database():
    connection = pymysql.connect(
        host='localhost',
        user='admin',
        password='mypasswordtext',  # Hardcoded password (insecure)
        db='my_database'
    )
    return connection

# Sim a database query
def fetch_data():
    conn = connect_to_database()
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM users")
            result = cursor.fetchall()
            print(result)
    finally:
        conn.close()

fetch_data()
