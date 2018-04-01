import requests
import sys
import random


class Client(object):
    ENDPOINT = 'http://127.0.0.1:5000'
    HASH = ''
    USERNAME = ''

    def __init__(self):
        self.HASH = self.generate_hash()
        # self.USERNAME = self.get_username()  TODO 

        requests.post('{}/register-seed'.format(self.ENDPOINT), data={'hash':self.HASH})


    def generate_hash(self):
        _hash = ''
        for i in range(20):
            _hash += str(int(random.random() * 10))
        return _hash
