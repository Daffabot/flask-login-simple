from flask import Flask, request, render_template, flash, redirect, jsonify
from passlib.hash import pbkdf2_sha256
import uuid, pymongo
app = Flask(__name__)
client = pymongo.MongoClient('localhost', 27017)
db = client.IOT_Control

# User Class
class User:
    def signup(self):
        print(request.form)

        # Create the user object
        user = {
            "id": uuid.uuid4().hex,
            "name": request.form.get('name'),
            "username": request.form.get('username'),
            "email": request.form.get('email'),
            "password": request.form.get('password'),
            "access": ""
        }

        # Encrypt the password
        user['password'] = pbkdf2_sha256.encrypt(user['password'])
        # Check for existing email address
        if db.person.find_one({ "email": user['email'] }):
            return jsonify({ "error": "Email address already in use" }), 400
        if db.users.insert_one(user):
            return jsonify(user), 200
        return jsonify({ "error": "Signup failed" }), 400

# main index
@app.route('/')
def index():
    return render_template('index.html',title="")

# admin login
@app.route('/admin/')
def adminIndex():
    return render_template('admin/index.html',title="Admin Login")

# ---------------------------user area----------------------------------

# user login
@app.route('/user/')
def userIndex():
    return render_template('user/index.html',title="User Login")

# user register
@app.route('/user/signup')
def userSignup():
    return render_template('user/signup.html',title="User Login")

# user register proses
@app.route('/user/prosignup', methods=['POST', 'GET'])
def signup():
    return User().signup()

if __name__=="__main__":
    app.run(debug=True)