# -*- coding: utf-8 -*-
# Time: 2021/5/21 20:15

import json
import re
from datetime import datetime, timedelta

from django import http
from django.conf import settings
from rest_framework.views import APIView

from users.models import User
from django.views import View
from django.contrib.auth import login, authenticate

from utils.JWTtokenUtil import generate_jwt


class LoginView(View):

    def _get_jwt_token(self, data, is_refresh=True):
        """
        生成token 和refresh_token
        :param user_id: 用户id
        :return: token, refresh_token
        """
        # 颁发JWT
        # now = datetime.utcnow()
        now = datetime.now()
        print(now)
        expiry = now + timedelta(hours=2)
        token = generate_jwt({'data': data, 'refresh': False}, expiry)
        refresh_token = None
        if is_refresh:
            refresh_expiry = now + timedelta(days=14)  # 刷新token有效期14天
            refresh_token = generate_jwt({'data': data, 'refresh': True}, refresh_expiry)
        return token, refresh_token

    def post(self, request):
        '''实现登录接口
        请求方法: POST
        参数类型: JSON
        '''
        # 接收参数
        try:
            dict = json.loads(request.body.decode())
        except json.decoder.JSONDecodeError:
            return http.JsonResponse({'code': 400, 'errmsg': '请求参数格式错误: JSON'})

        username = dict.get('username')
        password = dict.get('password')

        # 校验(整体 + 单个)
        if not all([username, password]):
            return http.JsonResponse({'code': 400, 'errmsg': '缺少必传参数'})

        # 验证是否能够登录(用于重写了authenticate认证接口,可以使用已经认证过得邮箱进行登录)
        user = authenticate(username=username, password=password)

        # 判断是否为空,如果为空,返回
        if user is None:
            return http.JsonResponse({'code': 400, 'errmsg': '用户名或者密码错误'})

        # 4.状态保持
        login(request, user)

        token, refresh_token = self._get_jwt_token(data={'user_id':user.id, 'username': user.username})

        return http.JsonResponse({'code': 201, 'errmsg': '登录成功',
                                  'token':token, 'refresh_token':refresh_token})

    # 更新token接口
    def put(self, request):
        user_id = request.user_id
        username = request.username
        is_refresh_token = request.is_refresh_token
        if user_id and is_refresh_token and username:
            token, refresh_token = self._get_jwt_token({'user_id':user_id, 'username': username}, is_refresh=False)
            return http.JsonResponse({'code': 201, 'token':token})
        else:
            return http.JsonResponse({'code': 403, 'errmsg': 'Wrong refresh token.'})


class RegisterView(View):
    """用户注册"""

    def post(self, request):
        data = json.loads(request.body.decode())
        username = data.get('username')
        password = data.get('password')
        password2 = data.get('password2')
        email = data.get('email')

        if not all([username, password, password2, email]):
            return http.JsonResponse({'code': 400, 'errmsg': '缺少参数！！！'})

        # 用户名 username 不可重复
        try:
            u_count = User.objects.filter(username=username).count()
        except Exception as e:
            return http.JsonResponse({'code': 400, 'errmsg': '用户名查询出错,稍后再试.'})
        #todo 后期给重复的username加上缓存
        if u_count >=1:
            return http.JsonResponse({'code': 400, 'errmsg': '用户名已存在！！！'})
        if not re.match(r'^[a-z0-9][\w\.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$', email):
            return http.JsonResponse({'code': 400, 'errmsg': '参数email格式有误'})

        if not re.match(r'^[a-zA-Z0-9]{6,20}$', password):
            return http.JsonResponse({'code': 400, 'errmsg': '密码格式有误'})
        if password !=password2:
            return http.JsonResponse({'code': 400, 'errmsg': '两次密码不同,请重新输入'})

        try:
            user = User.objects.create_user(username=username,
                                            password=password,
                                            email=email)
        except Exception as e:
            return http.JsonResponse({'code': 400, 'errmsg': '注册用户失败, 稍后再试.'})

        return http.JsonResponse({'code': 0, 'errmsg': 'ok'})

