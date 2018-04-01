# server.py
#
## KEEPS TRACK OF ALL THE SEED VALUES

from flask import Flask
app = Flask(__name__)


# List of all known seeds
SEEDS = []


@app.route('/register-seed')
def register_seed():
    seed_value = request.values['hash']
    return 'ok'


@app.route('/remove-seed')
def remove_seed():
    """ TODO """


