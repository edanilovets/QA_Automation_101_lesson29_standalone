import psycopg2

def test_database_connection():
    conn = psycopg2.connect(
        dbname="test_db",
        user="test_user",
        password="test_password",
        host="localhost",
        port="5432"
    )
    assert conn is not None

def test_data_insertion():
    conn = psycopg2.connect(
        dbname="test_db",
        user="test_user",
        password="test_password",
        host="localhost",
        port="5432"
    )
    cursor = conn.cursor()
    cursor.execute("CREATE DATABASE test_db IF NOT EXISTS")
    cursor.execute("INSERT INTO users (id, name) VALUES (1, 'John')")
    conn.commit()
    cursor.execute("SELECT * FROM users WHERE id=1")
    result = cursor.fetchone()
    assert result[1] == 'John'
