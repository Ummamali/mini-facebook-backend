from utils import bad_response, decode_token, generate_token, good_response
from flask import Flask, request, signals
from flask_cors import cross_origin
from jwt import exceptions as jwt_exp
from time import sleep


app = Flask(__name__)

user = {
    'id': 15543,
    'email': 'test@gmail.com',
    'password': 'test123'
}


@app.route('/login', methods=('POST', ))
@cross_origin()
def login():
    reqObj = request.get_json()
    email = reqObj['email']
    sleep(1)
    password = reqObj['password']
    if(email == user['email'] and password == user['password']):
        token = generate_token({'sub': user['id']})
        return good_response(payload={'token': token})
    else:
        return bad_response(msg='Not authorized')


@app.route('/changePswd', methods=('POST', ))
@cross_origin()
def change_password():
    reqObj = request.get_json()
    token = reqObj['token']
    new_password = reqObj['newPassword']
    sleep(1)
    try:
        payload = decode_token(token)
    except jwt_exp.InvalidSignatureError:
        return bad_response(status=401, msg='Invalid signature has been detected')
    except jwt_exp.DecodeError:
        return bad_response(status=401, msg='Error while decoding the token')
    except jwt_exp.ExpiredSignatureError:
        return bad_response(status=401, msg='Invalid token')
    else:
        user['password'] = new_password
        return good_response(msg='Password has been changed')


@app.route('/getPwd', methods=('POST', ))
@cross_origin()
def get_pwd():
    reqObj = request.get_json()
    token = reqObj['token']
    sleep(1)
    try:
        payload = decode_token(token)
    except jwt_exp.InvalidSignatureError:
        return bad_response(status=401, msg='Invalid signature has been detected')
    except jwt_exp.DecodeError:
        return bad_response(status=401, msg='Error while decoding the token')
    except jwt_exp.ExpiredSignatureError:
        return bad_response(status=401, msg='Invalid token')
    else:
        return good_response(msg='Password has been changed', payload={'password': user['password']})


if (__name__ == '__main__'):
    app.run(debug=True)
