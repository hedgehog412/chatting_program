import requests
import sys
import random
from flask import Flask
app=Flask(__name__)

class Client(object):
    ENDPOINT = 'http://127.0.0.1:5000'
    HASH = ''
    USERNAME = ''
    PORT=0
    PEERS=[]    

    def __init__(self):
        self.HASH = self.generate_hash()
        # self.USERNAME = self.get_username()  TODO 
        self.PORT=int(sys.argv[1])

        if random.random() < 0.5:
            print('Joining network as a seed')
            resp = requests.post('{}/register-seed'.format(self.ENDPOINT), data={'hash':self.HASH, 'port': self.PORT})
        else:
            print('Joining network as a peer')
            resp = requests.post('{}/join-net'.format(self.ENDPOINT), data={'hash': self.HASH, 'port': self.PORT})
            print(resp.text)
            self.PEERS.append(resp.text)
            temp='http://'+resp.text
            requests.post('{}/meet-peers'.format(temp),data={'hash':self.HASH,'port':self.PORT})

    def generate_hash(self):
        _hash = ''
        for i in range(20):
            _hash += str(int(random.random() * 10))
        return _hash

    def exit(self):
        requests.post('{}/remove-seed'.format(self.ENDPOINT),data={'hash':self.HASH})

    def join(self):
        seed_ip=requests.post('{}/join-net'.format(self.ENDPOINT),data={'hash':self.HASH,})
        print(seed_ip.text)

    @app.route('/meet-peers',methods=['POST'])
    def meet_peers(self):
        peer_value=request.values['hash']
        peer_port=request.values['port']
        peer_ip=request.remote_addr
        print('ok')
        self.PEERS.append('{}:{}'.format(peer_ip,peer_port))
        print(self.PEERS)
        return 'ok'

if __name__=='__main__':
    c=Client()
    app.run(host='127.0.0.1',port=c.PORT)
