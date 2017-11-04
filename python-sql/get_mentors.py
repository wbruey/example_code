import mysql.connector

connection=mysql.connector.connect(user='root',password='mAdultWill35!',host='localhost', database='rise')
cursor=connection.cursor()

query = ("SELECT first_name, last_name FROM mentor")

cursor.execute(query)

for (first_name, last_name) in cursor:
	print("{} {}".format(first_name,last_name))
	

cursor.close()
connection.close()


