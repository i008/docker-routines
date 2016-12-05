from flask import Flask

app1 = Flask(__name__)


@app1.route('/hello')
def hello():
    return "Hello from app1"


if __name__ == '__main__':
    app1.run(host='0.0.0.0', port=5000)

