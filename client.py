import requests
import sys
import random


class Client(object):
    ENDPOINT = 'http://127.0.0.1:5000'
    COOKIE = ''

    def __init__(self):
        self.generate_cookie()


    def generate_cookie(self):
        for i in range(10):
            self.COOKIE += str(int(random.random() * 10))

    def send_message(self, msg):
        resp = requests.post('{}/send-message'.format(self.ENDPOINT), data={'msg': msg, 'cookie': self.COOKIE})
        assert resp.text == 'Received'



    def get_message(self):
        resp = requests.get('{}/get-message'.format(self.ENDPOINT))

        messages = resp.text
        all_messages = messages.split('||')
        for message in all_messages:
            print 'NEW MSG: {}'.format(message)


    def main(self):
        print '**** WELCOME TO HEDGEHOG CHAT ****'
        print '**** PRESS q TO QUIT ****'
        print '**** PRESS r TO GET MESSAGE ****'
        print '**** OTHERWISE JUST TYPE AND PRESS ENTER TO SEND MESSAGE! ****'

        while True:
            sys.stdout.write('>> ')
            user_input = raw_input()

            if user_input == 'q':
                break

            if user_input == 'r':
                self.get_message()

            else:
                self.send_message(user_input)

if __name__ == '__main__':
    client = Client()

    client.main()
