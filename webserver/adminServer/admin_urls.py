# -*- coding: utf-8 -*-
# Time: 2021/5/18 17:28
# 博客管理后台的接口路由

from django.urls import path
from adminServer import admin_views

urlpatterns = [
    # 文章添加POST  与 文章列表接口GET
    path('article/', admin_views.ArticleListAPIView.as_view()),
    path('article/<int:pk>/', admin_views.ArticleDetailAPIView.as_view()),  # 文章详情
    path('tag/', admin_views.TagAPIView.as_view()),
    path('category/', admin_views.CategoryAPIView.as_view()),

]
