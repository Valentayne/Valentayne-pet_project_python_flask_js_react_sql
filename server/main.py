from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins="*")

users = {
    "stephan": "password123",
    "admin": "adminpass",
    "testuser": "testpass"
}

def validate_user(data, users):
    if data.get('key') in users and users[data['key']] == data.get('value'):
        return {"message": "Successfully logged in!"}
    return {"message": "Invalid login or password!"}


@app.route("/api/users", methods=['GET'])
def get_users():
    return jsonify({
        "users": [
            "arpan",
            "zach",
            "jessie"
        ]
    })

@app.route('/api/data', methods=['GET', 'POST'])
def get_data():
    if request.method == 'GET':
        return jsonify({'info': "some_staff", 'status': 1})
    if request.method == 'POST':
        data = request.get_json()
        response = validate_user(data, users)
        return jsonify(response)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)