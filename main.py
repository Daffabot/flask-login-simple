from flask import Flask, request, render_template
app=Flask(__name__)

@app.route('/admin/')
def adminIndex():
    return render_template('admin/index.html',
    title="Admin Login")


if __name__=="__main__":
    app.run(debug=True)