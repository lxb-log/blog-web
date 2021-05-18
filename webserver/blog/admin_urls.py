# -*- coding: utf-8 -*-
# Time: 2021/5/18 17:28
# 博客管理后台的接口路由

from django.urls import path
from blog import admin_views


urlpatterns = [
    path('books/', admin_views.ArticleListAPIView.as_view()),
    # path('books/(?P<pk>\d+)/', views.ArticleViewSet.as_view())
]
