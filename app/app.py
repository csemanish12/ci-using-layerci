from flask import Flask

app = Flask(__name__)


@app.route('/home')
def home():
    message = "hello worlds"
    return {"msg": message}


if __name__ == '__main__':
    app.run(port=5000, host="0.0.0.0")
