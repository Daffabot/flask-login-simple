from flask import Flask, request, render_template, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///ums.sqlite"
app.config["SECRET_KEY"]=""
db=SQLAlchemy(app)
bcrypt=Bcrypt(app)

# User Class
class User(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    fname=db.Column(db.String(255), nullable=False)
    lname=db.Column(db.String(255), nullable=False)
    username=db.Column(db.String(255), nullable=False)
    email=db.Column(db.String(255), nullable=False)
    edu=db.Column(db.String(255), nullable=False)
    password=db.Column(db.String(255), nullable=False)
    status=db.Column(db.Integer, default=1, nullable=False)

    def __repr__(self):
        return f'User("[self.id]", "[self.fname]", "[self.lname]", "[self.username]", "[self.email]", "[self.edu]", "[self.status]")'

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
@app.route('/user/signup', methods=['POST', 'GET'])
def userSignup():
    if request.methods=='POST':
        # Get all input field name
        fname=request.form.get('fname')
        lname=request.form.get('lname')
        username=request.form.get('username')
        email=request.form.get('email')
        edu=request.form.get('edu')
        password=request.form.get('password')

        # Check all field is it filled or not
        if fname=="" or lname=="" or username=="" or email=="" or edu=="" or password=="":
            flash('Please fill all field', 'danger')
            return redirect('/user/signup')
        else:
            hash_password=bcrypt.generate_password_hash(password, 10)
            # Belum selesai
    else:
        return render_template('user/signup.html',title="User Sign Up")

if __name__=="__main__":
    app.run(debug=True)