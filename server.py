#!/usr/bin/python3
from flask import Flask,jsonify
import os 

# os.mkdir(os.path.join(os.getcwd(),"volume"))

print('Reload...!!')
app = Flask(__name__)

@app.route('/api/v1/info',methods=['GET'])
def info():
    return jsonify({'status':'success','name':'ukrit Fongsomboon','data':1})

@app.route('/api/v1/getdata',methods=['GET'])
def getdata():
    return jsonify({'status':'success'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', threaded=True, port=5008)


# TODO Issue From Tue 01/09/63 Run Shell Scrip
## https://stackoverflow.com/quesdtions/9975011/pycharm-usr-bin-pythonm-bad-interpreter
## You may find the answers here: ./configure : /bin/sh^M : bad interpreter
## As a Mac OS X user, I didn't find the command dos2unix. Alternatively, I use vi/vim: :set fileformat=unix and then save the file :wq

# TODO how to create volume to docker area
## 1 Add Volume In Docekerfile 
#! VOLUME [ "/app" ]

## 2 create floder
#! mkdir data

## 3 Create Docker volume  
#! docker volume create --driver local --opt type=nfs --opt device=$(pwd)/data --opt o=bind,rw data

## 4 Run Container 
#! docker run --name testv -d -v data:/app -it ukrit