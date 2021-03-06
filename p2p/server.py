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

    # If we don't have any SEEDS, we treat this as a request to join as seed
    if len(SEEDS) == 0:
        seed_value = request.values['hash']
        seed_ip=request.remote_addr
        seed_port = request.values['port']
        SEEDS[seed_value] = '{}:{}'.format(seed_ip, seed_port)
        return 'ok'
       

    idx=int(random.random()*len(SEEDS))
    _hash=[]
    for key in SEEDS.keys():
        _hash.append(key)
    return SEEDS[_hash[idx-1]]

app.run()
