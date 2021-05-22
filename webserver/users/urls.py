# -*- coding: utf-8 -*-
# Time: 2021/5/21 20:16
# 用户接口路由

from django.urls import path
from users import views

urlpatterns = [
    # 注册
    path('register/', views.RegisterView.as_view()),
    path('login/', views.LoginView.as_view()),

]


