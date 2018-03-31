from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello'

@app.route('/bye')
def bye():
    return 'Bye'


app.run(host="0.0.0.0")


"""
class Server(object):
    @classmethod
    def register_client(cls):
        print 'Hello client'


    @classmethod
    def accept_conn(cls):
        print 'Connection accepted'


    @classmethod  # decorator
    def main(cls):
        print 'Hello, I am the server'

if __name__ == '__main__':
    app.run(
"""
