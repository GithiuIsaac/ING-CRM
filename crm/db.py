
import mariadb
import sys

# Instantiate Connection
try:
    database = mariadb.connect(
        host = 'localhost',
        port = 3306,
        user = 'admin',
        password = 'mariadb-admin'
        )
except mariadb.Error as e:
    print(f"Error connecting to the database: {e}")
    sys.exit(1)

# Prepare a Cursor Object
cursorObject = database.cursor()

# Create the DB
cursorObject.execute("CREATE DATABASE crm_db")

print("CRM Database Created")
