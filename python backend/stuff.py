import json
import sqlite3
# Open the JSON file in read mode
with open('D:\work\CRUD-vue-js\python backend\cringe.json', 'r') as file:
    # Load the contents of the file into a variable
    data = json.load(file)

# Now you can work with the data as a Python object
for i in data:
    data1 = i['title']
    data2 = i['body']
    conn = sqlite3.connect('new.db')
    conn.execute("INSERT INTO post (title,BODY) VALUES (?,?)", (data1,data2))
    conn.commit()
    conn.close()

