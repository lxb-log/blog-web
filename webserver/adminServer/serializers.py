
from rest_framework import serializers
from blog.models import Article, Tag



class SerializerTag(serializers.ModelSerializer):
    """ 标签序列化器类 """
    class Meta:
        model = Tag
        fields = ('id', 'name', 'created_time')


class SerializerPOSTArticle(serializers.ModelSerializer):
    """
        功能: 上传文章专用序列化器
    """

    class Meta:
        model = Article
        fields = '__all__'

        # 标题和摘要和标签和分类在创建文章对象时数据校验时不是必须传入
        extra_kwargs = {
            'desc': {
                'required': False
            },
            'tag': {
                'required': False
            },
            'category': {
                'required': False
            },
            'title': {
                'required': False
            },
        }


# 文章列表序列化器类
class SerializerArticleList(serializers.ModelSerializer):

    tag = SerializerTag(many=True)

    class Meta:
        model = Article
        fields = '__all__'
        extra_kwargs = {
            'content': {  # 设置为True，表明对应字段只在序列化操作时起作用
                'write_only': True
            },
        }



