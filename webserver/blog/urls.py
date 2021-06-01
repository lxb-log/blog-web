# -*- coding: utf-8 -*-
# Time: 2021/4/13 23:28

from django.urls import path
from blog import views


urlpatterns = [
    # 文章列表
    path('article/', views.ArticleListView.as_view()),
    # 文章详情
    path('article/<int:pk>/', views.ArticleDetailView.as_view()),

    # 分类
    path('category/', views.CategoryView.as_view()),
    # 标签
    path('tag/', views.TagView.as_view()),
]


