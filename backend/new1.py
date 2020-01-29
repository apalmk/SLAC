from flask import Flask, jsonify, request
import base64
from google.cloud import vision
from google.cloud.vision import types
import numpy as np
import testy as ts
# from keras.preprocessing import image

# from keras.models import load_model
# import predictor1 as pd

app = Flask(__name__)

# Elist = []
# FirstDict = {'mess':'Hello World'}
# Elist.append(FirstDict)
# jsonStr = json.dumps(employeeList)

# Str= 'Hello World'

@app.route('/start',methods=['GET'])
def test():
    # p=pd.pred()
    return jsonify(Mess="Hello")

@app.route('/presc',methods=['GET'])
def test1():
    # p=pd.pred()
    with open('pres.txt', 'r') as myfile:
        data = myfile.read().replace('\n', '; ')
    return jsonify(Mess=data)

@app.route("/imagec", methods=["POST"])
def handle_data():
    # l=str(request.args.get('query'))
    # json= request.get_json()
    f=request.files['image']
    f.seek(0)
    # print(f.read())
    ss=f.read()
    fh = open("fileee.jpg", 'wb')
    fh.write(ss)
    fh.close()
    j = ts.checker()
    # s=json['content']
    # s1 = str.encode(s)
    # with open("testImage.png", "wb") as fh:
    #     fh.write(base64.decodebytes(s1))
    # p = pd.pred()
    return jsonify(message=j)


if __name__ == '__main__':
    # app.debug = True
    app.run(host='0.0.0.0')