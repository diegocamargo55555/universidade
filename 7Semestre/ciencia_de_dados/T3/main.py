import mysql.connector

try:
    cnx = mysql.connector.connect(user='root', password='YourNewStrongPassword', host='127.0.0.1')

    # cnx = mysql.connector.connect(**config)

    # 2. Create a cursor object to interact with the server
    mycursor = cnx.cursor()

    # 3. Execute the SQL command to create the database
    # Using "IF NOT EXISTS" prevents errors if the DB already exists
    mycursor.execute("CREATE DATABASE IF NOT EXISTS my_new_db")

    print("Database created successfully!")

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    # 4. Clean up: close the cursor and connection
    if 'mycursor' in locals():
        mycursor.close()
    if 'cnx' in locals():
        cnx.close()





cnx.close()