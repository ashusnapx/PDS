from flask import Flask
from flask import request

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<h1> Hello, This is Ashutosh Kumar </h1>"


@app.route("/hello_world1")
def hello_world1():
    return "<h1> Hello, This is Ashutosh Kumar </h1>"


@app.route("/hello_world2")
def hello_world2():
    return "<h1> Hello, This is Ashutosh Kumar</h1>"


@app.route("/test")
def test():
    i = 10+7
    return "This is a test function created by chat gpt {}".format(i)


@app.route("/test2")
def test2():
    data = request.args.get('x')
    return 'this is the data input from my url {}'.format(data)


@app.route("/test3")
def test3():
    data = request.args.get('y')
    return 'Happy Birthday {} Bemta.'.format(data)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
