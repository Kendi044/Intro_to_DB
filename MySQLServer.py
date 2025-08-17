#!/usr/bin/env python3
CREATE DATABASE IF NOT EXISTS alx_book_store
import mysql.connector
from mysql.connector import errorcode

def create_database(user, password, host):
    """
    Connects to the MySQL server and creates the alx_book_store database if it doesn't exist.
    """
    try:
        # Connect to MySQL without specifying a database
        mydb = mysql.connector.connect(
            host=host,
            user=user,
            password=password
        )
        mycursor = mydb.cursor()

        db_name = "alx_book_store"

        # Use a parameterized query to create the database if it does not exist.
        # This is the standard and safest way to do this.
        sql = f"CREATE DATABASE IF NOT EXISTS {db_name}"
        mycursor.execute(sql)
        
        print(f"Database '{db_name}' created successfully!")
        
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(f"Error: {err}")
    
    finally:
        # Close the connection
        if 'mydb' in locals() and mydb.is_connected():
            mycursor.close()
            mydb.close()
            
if __name__ == "__main__":
    # You need to replace these with your actual MySQL credentials
    db_user = "root"
    db_password = "password"
    db_host = "localhost"  # Or your MySQL server's IP address if it's not local
    create_database(db_user, db_password, db_host)
