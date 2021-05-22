
from rest_framework.views import APIView
from rest_framework.response import Response
from adminServer.serializers import SerializerPOSTArticle, SerializerArticleList
from blog.models import Article
from rest_framework import status


class ArticleListAPIView(APIView):
    """视图集"""

    def get(self, request):
        """
        获取所有的文章数据
        """
        queryset = Article.objects.all()
        # 序列化所有数据
        serializer = SerializerArticleList(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        """
        新增
        """
        # 反序列化-数据校验
        data = request.data
        data['owner'] = 1
        print(data.get('desc'))
        serializer = SerializerPOSTArticle(data=data)
        serializer.is_valid(raise_exception=True)
        # article = serializer.save()

        # 反序列化-数据保存(save内部会调用序列化器类的create方法)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)