import requests
import sys
import random


class Client(object):
    ENDPOINT = 'http://127.0.0.1:5000'
    COOKIE = ''
    USERNAME = ''
    def __init__(self):
        self.generate_cookie()
        self.USERNAME=self.get_username()
        requests.post(self.ENDPOINT,data={'cookie':self.COOKIE,'username':self.USERNAME})    

    def generate_cookie(self):
        for i in range(10):
            self.COOKIE += str(int(random.random() * 10))

    def get_username(self):
        print('Enter username')
        user_input=input()
        return user_input

    def send_message(self, msg):
        resp = requests.post('{}/send-message'.format(self.ENDPOINT), data={'msg': msg, 'cookie': self.COOKIE,'username':self.USERNAME})
        assert resp.text == 'Received'



    def get_message(self):
        resp = requests.post('{}/get-message'.format(self.ENDPOINT),data={'cookie':self.COOKIE})

        messages = resp.text
        all_messages = messages.split('||')
        for message in all_messages:
            print(message)


    def main(self):
        print ('**** WELCOME TO HEDGEHOG CHAT ****')
        print ('**** PRESS q TO QUIT ****')
        print ('**** PRESS r TO GET MESSAGE ****')
        print ('**** OTHERWISE JUST TYPE AND PRESS ENTER TO SEND MESSAGE! ****')

        while True:
            sys.stdout.write('>> ')
            user_input = input()

            if user_input == 'q':
                break

            if user_input == 'r':
                self.get_message()

            else:
                self.send_message(user_input)

if __name__ == '__main__':
    client = Client()

    client.main()
