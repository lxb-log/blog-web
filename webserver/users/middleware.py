# -*- coding: utf-8 -*-
# Time: 2021/5/22 21:54
from django.conf import settings
from django.utils.deprecation import MiddlewareMixin

from utils.JWTtokenUtil import verify_jwt

"""
由于我没有使用Django自带的session认证与没有使用DRF框架扩展的JWT认证
so, 我自己写了一个认证中间件, 让django根据我的验证规则, 去判断用户是否登录,
以及确定当前登录的用户是哪个
"""


class DIYAuthenticatedMiddlewareMixin(MiddlewareMixin):

    def process_request(self, request):
        authorization = request.headers.get('Authorization')
        # request.user = None
        request.user_id = None
        request.username = None
        request.is_refresh_token = False  # 是否是刷新token

        if authorization and authorization.startswith('Tomato '):
            jwt_token = authorization.strip()[7:]
            payload = verify_jwt(token=jwt_token)
            if payload:
                request.is_refresh_token = payload.get('refresh', False)
                data = payload.get('data', None)
                print(payload)
                if data is not None:
                    request.user_id = data.get('user_id', None)
                    request.username = data.get('username', None)



    # 暂时没用的响应中间件
    # def process_response(self, request, response):
    #     # print("process_response")
    #     return response

