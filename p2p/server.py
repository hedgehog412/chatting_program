# server.py
#
## KEEPS TRACK OF ALL THE SEED VALUES

from flask import Flask,request
app = Flask(__name__)


# List of all known seeds
SEEDS = []
@app.route('/register-seed',methods=['GET','POST'])
def register_seed():
    seed_value = request.values['hash']
    seed_ip=request.remote_addr
    print(seed_ip)
    seed_port=request.environ.get('REMOTE_PORT')
    SEEDS.append(seed_value)
    return 'ok'


@app.route('/remove-seed')
def remove_seed():
    SEEDS.remove(request.values['hash'])

@app.route('/join-net')
def register_peer():
    idx=int(random.random()*len(SEEDS))
    
    return SEEDS[idx]
app.run()
