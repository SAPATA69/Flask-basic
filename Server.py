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
    <h1>Welcome to the Server application!</h1>
</body>
</html>
"""

@app.route('/user/<username>')
def user(username):
    return f'<h1>My name is {username}!!</h1>'

# ✅ แก้ไขแล้ว: แยก route และชื่อ function ให้ถูกต้อง
@app.route('/calculate/addition/<int:a>/<int:b>')
def addition(a, b):
    result = a + b
    return f'<h1>{a} + {b} = {result}</h1>'

@app.route('/calculate/subtraction/<int:a>/<int:b>')
def subtraction(a, b):
    result = a - b
    return f'<h1>{a} - {b} = {result}</h1>'

@app.route('/calculate/multiplication/<int:a>/<int:b>')
def multiplication(a, b):
    result = a * b
    return f'<h1>{a} × {b} = {result}</h1>'

@app.route('/calculate/division/<int:a>/<int:b>')
def division(a, b):
    result = a / b
    return f'<h1>{a} ÷ {b} = {result:.2f}</h1>'


@app.route('/secretkey/<uuid:sk>')
def my_secretkey(sk):
    return f'<h1>Your secret key is {sk}</h1>'


if __name__ == '__main__':
    app.run(debug=True)