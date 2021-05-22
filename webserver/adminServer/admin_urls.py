# -*- coding: utf-8 -*-
# Time: 2021/5/18 17:28
# 博客管理后台的接口路由

from django.urls import path
from adminServer import admin_views

urlpatterns = [
    # 文章添加POST  与 文章列表接口GET
    path('article/', admin_views.ArticleListAPIView.as_view()),
    # path('books/(?P<pk>\d+)/', views.ArticleViewSet.as_view())
]
