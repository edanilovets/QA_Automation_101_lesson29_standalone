import allure
import psycopg2
import pytest


@allure.epic("Database Epic")
@allure.feature("Database Feature")
class TestDatabase:
    @pytest.mark.skip("Database connection is not available")
    def test_database_connection():
        # Connect to the PostgreSQL default database
        conn = psycopg2.connect(
            dbname="postgres",  # Connect to default 'postgres' database to check and create test_db
            user="test_user",
            password="test_password",
            host="localhost",
            port="5432"
        )
        conn.autocommit = True
        cursor = conn.cursor()

        # Check if the database exists
        cursor.execute(
            "SELECT 1 FROM pg_database WHERE datname = 'test_db'"
        )
        exists = cursor.fetchone()
        if not exists:
            cursor.execute("CREATE DATABASE test_db")
        cursor.close()
        conn.close()

        # Assert that the database connection is successful
        conn = psycopg2.connect(
            dbname="test_db",  # Now connect to 'test_db'
            user="test_user",
            password="test_password",
            host="localhost",
            port="5432"
        )
        assert conn is not None
        conn.close()

    @pytest.mark.skip("Database connection is not available")
    def test_data_insertion():
        # Connect to the test_db
        conn = psycopg2.connect(
            dbname="test_db",
            user="test_user",
            password="test_password",
            host="localhost",
            port="5432"
        )
        conn.autocommit = True
        cursor = conn.cursor()

        # Create the 'users' table if it does not exist
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                name TEXT NOT NULL
            )
            """
        )

        # Insert data into the 'users' table
        cursor.execute("INSERT INTO users (id, name) VALUES (1, 'John') ON CONFLICT (id) DO NOTHING")
        conn.commit()

        # Verify the data insertion
        cursor.execute("SELECT * FROM users WHERE id=1")
        result = cursor.fetchone()
        assert result is not None
        assert result[1] == 'John'

        cursor.close()
        conn.close()
