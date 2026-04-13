import mysql.connector

cnx = mysql.connector.connect(user='root', password='YourNewStrongPassword', host='127.0.0.1')

# cnx = mysql.connector.connect(**config)


cnx.close()