from flask import Flask, request, jsonify
from flask_cors import CORS
import psycopg2
import os

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASSWORD")
DB_PORT = "5432"
DB_HOST = os.getenv("DB_HOST")

try:
    conn = psycopg2.connect(database=DB_NAME,
                             user=DB_USER,
                             password=DB_PASS,
                             host=DB_HOST,
                             port=DB_PORT)
    print("Database connected successfully")
except Exception as e:
    print("Database not connected successfully:", str(e))
    conn = None

app = Flask(__name__)
CORS(app, origins="*")

def validate_user(data, users):
    if data.get('key') in users and users[data['key']] == data.get('value'):
        return {"message": "Successfully logged in!"}
    return {"message": "Invalid login or password!"}

@app.route('/api/data', methods=['GET', 'POST'])
def get_data():
    if request.method == 'GET':
        return jsonify({'info': "some_staff", 'status': 1})
    
    if request.method == 'POST':
        data = request.get_json()

        if conn is None:
            return jsonify({"error": "Database connection failed"}), 500
        
        try:
            cur = conn.cursor()
            cur.execute("SELECT full_name, password_hash FROM users")
            db_users = cur.fetchall()
            cur.close()
            users = {user[0]: user[1] for user in db_users}
            response = validate_user(data, users)
            return jsonify(response)
        
        except Exception as e:
            return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
