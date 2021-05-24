
from rest_framework import serializers
from blog.models import Article, Tag, Category


class SerializerCategory(serializers.ModelSerializer):
    """ 分类序列化器类 """
    class Meta:
        model = Category
        fields = ('id', 'name', 'owner', 'in_nav', 'created_time')
        extra_kwargs = {
            'owner': {  # 设置为True，表明对应字段只在序列化操作时起作用
                'write_only': True
            },
            'in_nav': {   # 该字段可不传
                'required': False
            },
        }



class SerializerTag(serializers.ModelSerializer):
    """ 标签序列化器类 """
    class Meta:
        model = Tag
        fields = ('id', 'name', 'owner', 'created_time')
        extra_kwargs = {
            'owner': {  # 设置为True，表明对应字段只在序列化操作时起作用
                'write_only': True
            },
        }


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
    category = SerializerCategory()

    class Meta:
        model = Article
        fields = '__all__'
        extra_kwargs = {
            'content': {  # 设置为True，表明对应字段只在序列化操作时起作用
                'write_only': True
            },
        }


# 文章详情序列化器类
class SerializerArticleDetail(serializers.ModelSerializer):
    tag = SerializerTag(many=True)
    category = SerializerCategory()

    class Meta:
        model = Article
        fields = '__all__'


