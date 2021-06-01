from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views import View

from blog.models import Article, Category, Tag
from utils.paging import pager_limit


class ArticleListView(View):
    def get(self, request):
        queryset = Article.objects.filter(status=1).select_related("category")
        qs, meta = pager_limit(request, queryset)
        # 序列化所有数据
        data = [q.serialization() for q in qs]
        return JsonResponse({'data': data, 'meta': meta, "code": 200})


class ArticleDetailView(View):
    def get(self, request, pk):
        article = get_object_or_404(Article, pk=pk)
        data = article.serialization(detail=True)
        return JsonResponse({'data': data, "code": 200})


class CategoryView(View):
    def get(self, request):
        queryset = Category.objects.all()
        data = [q.serialization() for q in queryset]
        return JsonResponse({'data': data, "code": 200})


class TagView(View):
    def get(self, request):
        queryset = Tag.objects.all()
        data = [q.serialization() for q in queryset]
        return JsonResponse({'data': data, "code": 200})