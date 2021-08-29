from flask import Flask, request, jsonify

import os, ast,shutil
import json, pickle

app = Flask(__name__)


@app.route('/status', methods = ['GET'])
def service_status():
    return "service is executing"

@app.route('/creatuser', methods = ['POST'])
def create_file():

    req = request.json
    userid= req['userid']
    with open("C:/Users/aravi/Downloads/Day2 Notes/sample.txt") as rf:
        rf.write(userid)   
    return "file created"
@app.route('/predict', methods = ['POST'])
def predict_GPA():

    req = request.json
    score= req['score']
    pickel_m = "C:/Users/aravi/Downloads/Day2 Notes/satmodel.pkl"
    with open(pickel_m, 'rb') as file:  
        load_model = pickle.load(file)
        result = load_model.predict([[score]])
    return  str(result[0][0]) 

print(__name__)
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=7002,debug=False,threaded=True)








@app.route('\createuser',methods = ['POST'])
def create_user():
    req = request.json
    userid = req['userid']
    with open ("C:\Users\aravi\Downloads\Day2 Notes\samples.txt") as rf:
        rf.write(userid)
    return "file created" 