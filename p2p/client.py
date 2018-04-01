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

if __name__=='__main__':
    c=Client()
    app.run(host='127.0.0.1',port=c.PORT)
