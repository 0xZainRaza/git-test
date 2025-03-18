import sqlite3
import os
from flask import Flask, request

app = Flask(__name__)

# Initialize database
conn = sqlite3.connect("users.db", check_same_thread=False)
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)")
conn.commit()

@app.route('/login', methods=['GET'])
def login():
    username = request.args.get('username')
    password = request.args.get('password')

    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    print(f"Executing query: {query}")  # Debugging purpose
    cursor.execute(query)
    user = cursor.fetchone()

    if user:
        return "Login Successful"
    else:
        return "Invalid Credentials"

@app.route('/ping', methods=['GET'])
def ping():
    ip = request.args.get('ip')
    response = os.popen(f"ping -c 1 {ip}").read()
    return f"<pre>{response}</pre>"

if __name__ == '__main__':
    app.run(debug=True)
