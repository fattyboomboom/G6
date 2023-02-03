from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'this is test 2'

@app.route('/hi')
def test():
    return 'test 3'

@app.route('/hi/hello')
def test2():
    return 'test 4'