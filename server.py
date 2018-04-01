from flask import Flask, request
app = Flask(__name__)

data_storage = {}

@app.route('/',methods=['POST'])
def init():
    data=request.values
    data_storage[data['cookie']]=[]
    return 'okay'
@app.route('/send-message', methods=['POST'])
def hello():
    data = request.values
        
    for key in data_storage:
        if key != data['cookie']:
            data_storage[key].append(data['username']+': '+data['msg'])
    return 'Received'


@app.route('/get-message',methods=['POST'])
def get_message():
    messages = ''
    data = request.values
    for i in range(len(data_storage[data['cookie']])):
        msg = data_storage[data['cookie']].pop(0)
        messages += msg
        messages += '||'

    return messages


@app.route('/bye')
def bye():
    return 'Bye'


app.run(host="0.0.0.0")
