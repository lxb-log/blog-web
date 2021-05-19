
from rest_framework import serializers
from blog.models import Article, Tag



class SerializerTag(serializers.ModelSerializer):
    """ 标签序列化器类 """
    class Meta:
        model = Tag
        fields = ('id', 'name', 'created_time')


class SerializerListArticle(serializers.ModelSerializer):
    """ 文章列表与上传序列化器类
        功能: 上传, 获取文章列表
    """

    # 设置为True，表明对应字段只在序列化操作时起作用
    tag = SerializerTag(many=True)
    content =  serializers.CharField(write_only=True, help_text='MarkDown格式', label='正文', style={'base_template': 'textarea.html'})

    class Meta:
        model = Article
        fields = '__all__'





