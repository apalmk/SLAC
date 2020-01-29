from flask import Flask, jsonify, request
import base64
# import base64
import io
import numpy as np
from base64 import decodestring
import cv2
import json
import tensorflow as tf
from keras import backend as K
import findstudent as f
from werkzeug.datastructures import ImmutableMultiDict
import PIL.Image as Image
from smsframework import Gateway
# from smsframework_clickatell import ClickatellProvider
from smsframework import OutgoingMessage
from twilio.rest import Client

def sendsms():
    account_sid = 'AC5e33c84748fe3102465e5459e012dab0'
    auth_token = '9911d22793656f50a136e26040f663c1'
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="Hi Anjani Your password is \"pass\"",
        from_='+17177272022',
        to='+91 9790650451'
    )
    return message.sid

app = Flask(__name__)

Str= 'Hello World'

@app.route('/start',methods=['GET'])
def test():
    # p=pd.pred()
    return jsonify(Mess="Hello")

@app.route('/forgot',methods=['GET'])
def forgot():
    # p=pd.pred()
    msg1=sendsms()
    return msg1

@app.route("/register", methods=["POST"])
def handle_data():
    # l=str(request.args.get('query'))
    json1= request.get_json()
    s=json1['regdata']
    my_list = s.split(",")
    print(my_list[0],my_list[1],my_list[2],my_list[3])

    data = {}
    data['people'] = []
    data['people'].append({
        'name': my_list[0],
        'pass': my_list[1],
        'em': my_list[2],
        'fac': my_list[3]
    })

    with open('data.txt', 'w') as outfile:
        json.dump(data, outfile)
    return "sucess"

@app.route("/recog", methods=["POST"])
def get_face():
    # l=str(request.args.get('query'))
    # data=request.data()
    # print(request.form)
    data = dict(request.form)
    # print(type(data['check']))
    imgdata = base64.b64decode(data['check'])
    filename = 'imageee.png'  # I assume you have a way of picking unique filenames
    with open(filename, 'wb') as f:
        f.write(imgdata)
    return jsonify(message="Done")

@app.route("/test", methods=["POST"])
def get_face1():
    K.clear_session()
    tf.keras.backend.clear_session()
    js=request.get_json()
    name=f.findd()
    tf.keras.backend.clear_session()
    K.clear_session()
    return name

@app.route("/login", methods=["POST"])
def handle_data1():
    json2= request.get_json()
    s=json2['login']
    my_list1 = s.split(",")
    print(json2)
    cs="nf"
    rs="11"
    with open('data.txt') as json_file:
        data = json.load(json_file)
        for p in data['people']:
            if p['name']==my_list1[0]:
                cs=p['pass']
        if cs=="nf":
            rs="10"
        else:
            if cs==my_list1[1]:
                rs="01"

            else:
                rs="00"

    return rs


if __name__ == '__main__':
    # app.debug = True
    app.run(host='0.0.0.0',port='5000',debug='True')
