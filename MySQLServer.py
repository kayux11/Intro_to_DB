# MySQLServer.py

import mysql.connector

def create_database():
    try:
        # Connect to MySQL server (update user & password as needed)
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="your_password"
        )

        if connection.is_connected():
            cursor = connection.cursor()
            # Create database if not exists (no SELECT or SHOW used)
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as e:
        print(f"Error while connecting to MySQL: {e}")

    finally:
        # Close connection
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            # Optional: print("MySQL connection closed.")

if __name__ == "__main__":
    create_database()
