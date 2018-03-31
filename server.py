from flask import Flask, request
app = Flask(__name__)

data_storage = []

@app.route('/send-message', methods=['GET', 'POST'])
def hello():
    data = request.values
    data_storage.append(data['msg'])
    print data['cookie']
    return 'Received'


@app.route('/get-message')
def get_message():
    messages = ''
    
    for i in range(len(data_storage)):
        msg = data_storage.pop(0)
        messages += msg
        messages += '||'

    return messages


@app.route('/bye')
def bye():
    return 'Bye'


app.run(host="0.0.0.0")
