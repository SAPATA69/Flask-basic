from flask import Flask
import uuid

app = Flask(__name__)


@app.route('/name')
def index():
    
    return f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>Welcome to the Sever application!</h1>
</body>
</html>
"""

@app.route('/user/<username>')
def user(username):
    
    return f'<h1>my name is, {username}!!</h1>'

@app.route('/calculate/addition/<int:a>/<int:b>')
def addition(a, b):
    result = a + b
    return f'<h1>{a} + {b} = {a+b}</h1>'

@app.route('/calculate/addition/<int:a>/<int:b>')
def addition(a, b):
    result = a - b
    return f'<h1>{a} - {b} = {a-b}</h1>'

@app.route('/calculate/addition/<int:a>/<int:b>')
def addition(a, b):
    result = a * b
    return f'<h1>{a} * {b} = {a*b}</h1>'


@app.route('/secretkey/<uuid:sk>')
def my_secretkey(sk):
    return f'<h1>your secret key is {sk}</h1>'



if __name__ == '__main__':
    app.run(debug=True)

    # if __name__ == '__main__':
    #     app.run(host='