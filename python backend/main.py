from flask import Flask, jsonify,request
from flask_cors import CORS, cross_origin
# import Functions
import sqlite3

conn = sqlite3.connect('new.db', timeout=5.0)


app = Flask(__name__)
app.config['CORS_METHODS'] = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
CORS(app)

@app.route('/api/message')
def message():
    response = jsonify({'message': 'Hello, world!'})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/api/hello')
def hello():
    response = jsonify({'message': 'Hello!'})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/api/delete/<id>', methods=["DELETE"])
def deletePost(id):
    pID = id
    conn.execute("DELETE FROM post WHERE id = ?", pID)
    conn.commit()
    conn.close()
    return 'Deleted post'


@app.route('/api/post/<id>', methods=['GET'])
@cross_origin()
def getPost(id):
    pID = id
    data = conn.execute("SELECT * FROM post WHERE id = "+ pID)
    print(data)
    conn.commit()
    conn.close() 
    return data

@app.route('/api/posts', methods=['GET'])
@cross_origin()
def getPosts():
    data = conn.execute("SELECT * FROM post").fetchall()
    conn.commit()
    conn.close()
    print(data)
    return data

@app.route('/upload', methods=['POST'])
@cross_origin()
def Addpost():
    data = request.json
    data1 = data.get('data1')
    data2 = data.get('data2')

    print(data1 , data2)
    conn.execute("INSERT INTO post (title,BODY) VALUES (?,?)", (data1,data2))
    conn.commit()
    conn.close()
    return 'data added'



if __name__ == '__main__':
    app.run()

