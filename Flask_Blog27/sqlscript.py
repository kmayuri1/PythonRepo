import json
import mysql.connector


with open(r'C:\Users\mayur\Python_3oct\postdata.json', 'r',encoding='utf-8') as json_file:
    data = json.load(json_file)


db_connection = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="sqluser1",
    password="password",
    database="newdb"
)
#sqluser1:password@localhost:3306/newdb'
# Create a cursor
cursor = db_connection.cursor()

for item in data:
    
    sql = "INSERT INTO Post (title, content, user_id) VALUES (%s, %s, %s)"
    values = (item['title'], item['content'], item['user_id'])
    cursor.execute(sql, values)


db_connection.commit()
cursor.close()
db_connection.close()
