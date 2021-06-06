from flask import jsonify
from jwt import encode, decode
from datetime import date, datetime, timedelta


key = 'laksjdlsadj'
token_leese = timedelta(minutes=1)


def good_response(payload=None, status=200, msg='Success!!!'):
    return jsonify({'payload': payload, 'status': status, 'msg': msg})


def bad_response(payload=None, status=400, msg='Failed!!!'):
    return jsonify({'payload': payload, 'status': status, 'msg': msg})


def generate_token(payload):
    payload['exp'] = datetime.utcnow() + token_leese
    return encode(payload, key, algorithm='HS256')


def decode_token(token):
    return decode(token, key, algorithms=['HS256'])
