
from rest_framework.views import APIView
from rest_framework.response import Response
from adminServer.serializers import SerializerPOSTArticle, SerializerArticleList, SerializerTag, SerializerCategory, \
    SerializerArticleDetail
from blog.models import Article, Tag, Category
from rest_framework import status

from utils.paging import pager_limit


class CategoryAPIView(APIView):
    def get(self, request):
        queryset = Category.objects.all().order_by("-status", "-created_time")
        serializer = SerializerCategory(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        data['owner'] = request.user_id
        serializer = SerializerCategory(data=data)
        serializer.is_valid(raise_exception=True)
        # 反序列化-数据保存(save内部会调用序列化器类的create方法)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CategoryDetailAPIView(APIView):

    def put(self, request, pk):
        try:
            queryset = Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            return Response({'code': 404, 'errmsg': '文章分类不存在'})

        data = request.data
        try:
            data['owner'] = request.user_id
        except Exception as e:
            return Response({"errmsg": "参数传递方式错误, 请使用JSON格式! "}, status=status.HTTP_402_PAYMENT_REQUIRED)

        serializer = SerializerCategory(instance=queryset, data=data)
        serializer.is_valid(raise_exception=True)
        # 反序列化-数据保存(save内部会调用序列化器类的create方法)
        serializer.save()

        return Response({'errmsg': '保存成功'}, status=status.HTTP_201_CREATED)


# 标签
class TagAPIView(APIView):
    def get(self, request):
        queryset = Tag.objects.all().order_by("-status", "-created_time")
        serializer = SerializerTag(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        data['owner'] = request.user_id
        # print(data["owner_id"])
        serializer = SerializerTag(data=data)
        serializer.is_valid(raise_exception=True)

        # 反序列化-数据保存(save内部会调用序列化器类的create方法)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class TagDetailAPIView(APIView):

    def put(self, request, pk):
        try:
            queryset = Tag.objects.get(pk=pk)
        except Tag.DoesNotExist:
            return Response({'code': 404, 'errmsg': '文章标签不存在'})

        data = request.data
        try:
            data['owner'] = request.user_id
        except Exception as e:
            return Response({"errmsg": "参数传递方式错误, 请使用JSON格式! "}, status=status.HTTP_402_PAYMENT_REQUIRED)

        serializer = SerializerTag(instance=queryset, data=data)
        serializer.is_valid(raise_exception=True)
        # 反序列化-数据保存(save内部会调用序列化器类的create方法)
        serializer.save()

        return Response({'errmsg': '保存成功'}, status=status.HTTP_201_CREATED)

# 文章详情
class ArticleDetailAPIView(APIView):
    def get(self, request, pk):
        """
        获取文章详情
        """
        try:
            queryset = Article.objects.get(pk=pk)
        except Article.DoesNotExist:
            return Response({'code': 404, 'errmsg': '文章不存在'})
        # 序列化所有数据
        serializer = SerializerArticleDetail(queryset)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            queryset = Article.objects.get(pk=pk)
        except Article.DoesNotExist:
            return Response({'code': 404, 'errmsg': '文章不存在'})

        data = request.data
        # data['owner'] = request.user_id
        try:
            data['owner'] = 1
        except Exception as e:
            return Response({"errmsg": "参数传递方式错误, 请使用JSON格式! "}, status=status.HTTP_402_PAYMENT_REQUIRED)

        serializer = SerializerPOSTArticle(instance=queryset,data=data)
        serializer.is_valid(raise_exception=True)
        # 反序列化-数据保存(save内部会调用序列化器类的create方法)
        serializer.save()

        return Response({'errmsg': '保存成功'}, status=status.HTTP_201_CREATED)


# from rest_framework.pagination import PageNumberPagination
#
# class StandardResultPagination(PageNumberPagination):
#     # 指定分页的默认页容量
#     page_size = 3
#     # 指定获取分页数据时，页容量参数的名称
#     # 注意：下面这个属性不要写成：page_query_param
#     page_size_query_param = 'pagesize'
#     # 指定分页时的最大页容量
#     max_page_size = 5

# 文章

class ArticleListAPIView(APIView):
    """视图集"""

    def get(self, request):
        """
        获取所有的文章数据
        """

        queryset = Article.objects.all()
        # 分页
        qs, meta = pager_limit(request, queryset)
        # 序列化所有数据
        serializer = SerializerArticleList(qs, many=True)
        return Response({'data': serializer.data, 'meta': meta})

    def post(self, request):
        """
        新增
        """
        # 反序列化-数据校验
        data = request.data
        # data['owner'] = request.user_id
        try:
            data['owner'] = 1
        except Exception as e:
            return Response({"errmsg": "参数传递方式错误, 请使用JSON格式! "}, status=status.HTTP_402_PAYMENT_REQUIRED)
        serializer = SerializerPOSTArticle(data=data)
        serializer.is_valid(raise_exception=True)
        # article = serializer.save()

        # 反序列化-数据保存(save内部会调用序列化器类的create方法)
        serializer.save()

        return Response({'errmsg': '保存成功'}, status=status.HTTP_201_CREATED)


