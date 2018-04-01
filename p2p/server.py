# server.py
#

## KEEPS TRACK OF ALL THE SEED VALUES

import random

from flask import Flask,request
app = Flask(__name__)


# List of all known seeds
SEEDS = {}
@app.route('/register-seed',methods=['GET','POST'])
def register_seed():
    seed_value = request.values['hash']
    seed_ip=request.remote_addr
    seed_port = request.values['port']
    SEEDS[seed_value] = '{}:{}'.format(seed_ip, seed_port)
    print(seed_port)
    return 'ok'


@app.route('/remove-seed')
def remove_seed():
    SEEDS.remove(request.values['hash'])

@app.route('/join-net', methods=['GET', 'POST'])
def register_peer():
    idx=int(random.random()*len(SEEDS))
    
    _hash = SEEDS.keys()[idx]
    return SEEDS[_hash]

app.run()
