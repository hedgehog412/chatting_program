import requests
import sys
import random
from flask import Flask, request

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

            if resp.text == 'ok':  # this means we joined the network as the seed, not peer
                return

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

    def meet_peers(self, peer_value, peer_port, peer_ip):
        print('ok')
        all_peers = str(self.PEERS)
        self.PEERS.append('{}:{}'.format(peer_ip,peer_port))
        return all_peers

app=Flask(__name__)
c=Client()

@app.route('/meet-peers',methods=['POST'])
def meet_peers_endpoint():
    peer_value=request.values['hash']
    peer_port=request.values['port']
    peer_ip=request.remote_addr
    return c.meet_peers(peer_value, peer_port, peer_ip)
   

if __name__=='__main__':
    app.run(host='127.0.0.1',port=c.PORT)
