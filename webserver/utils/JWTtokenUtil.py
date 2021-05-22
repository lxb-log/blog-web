# -*- coding: utf-8 -*-
# Time: 2021/5/21 23:12
from datetime import datetime, timedelta

import jwt
from django.conf import settings


def generate_jwt(payload, expiry, secret=None):
    """
    生成jwt
    :param payload: dict 载荷
    :param expiry: datetime 有效期
    :param secret: 密钥
    :return: jwt
    """
    _payload = {
        'exp': expiry,  # 过期时间
        'iss': 'lxb_wyf@163.com',  # 签名 #todo后期
    }
    _payload.update(payload)

    if not secret:
        secret = settings.SECRET_KEY

    token = jwt.encode(_payload, secret, algorithm='HS256')  # 加密生成字符串

    return token

def verify_jwt(token, secret=None):
    """
    检验jwt
    :param token: jwt
    :param secret: 密钥
    :return: dict: payload
    """
    if not secret:
        secret = settings.SECRET_KEY
    try:
        payload = jwt.decode(token, secret, algorithms=['HS256'])
    except jwt.PyJWTError as e:
        payload = None

    return payload


if __name__ == '__main__':
    import jwt
    import datetime
    now = datetime.datetime.now()
    print(now)
    expiry = now + timedelta(hours=2)
    secret = "django-insecure-f4gui6u3)*)0bz9$-^0q^&mr_2tbf97)bmo$+5s+)7w4tci2-4"
    token = generate_jwt(payload={'user1': 112}, expiry=expiry, secret=secret)
    print(token)
    print(type(token))
    token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2MjE2OTIyMDYsImlzcyI6Imx4Yl93eWZAMTYzLmNvbSIsImRhdGEiOnsidXNlcl9pZCI6MSwidXNlcm5hbWUiOiJcdTg0ZGRcdTVjMGZcdTc2N2QifSwicmVmcmVzaCI6ZmFsc2V9.rwYirbBFpfSwElHaenw_MV9WU2LEH-uBx6CR8qhCwvw"
    print(token)
    print(type(token))
    print("***")
    print(verify_jwt(token=token, secret=secret))
    print("***")


