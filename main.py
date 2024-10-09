from flask import Flask, request, render_template
app=Flask(__name__)

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

if __name__=="__main__":
    app.run(debug=True)