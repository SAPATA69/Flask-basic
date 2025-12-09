from flask import Flask

app = Flask(__name__)

@app.route('/name')
def index():
    return 'Welcome to the Sever application!'

if __name__ == '__main__':
    app.run(debug=True)

    # if __name__ == '__main__':
    #     app.run(host='