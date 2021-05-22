
from django.db import models

# Create your models here.
from users.models import User


class CreatedTime(models.Model):
    # 创建时间
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    class Meta:
        abstract = True  # 忽略这个模型类(不创建表), 这个模型类只做辅助作用


class Category(CreatedTime):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        (STATUS_DELETE, "删除"),
        (STATUS_NORMAL, "正常")
    )

    name = models.CharField(max_length=75, verbose_name="名称")
    status = models.PositiveBigIntegerField(default=STATUS_NORMAL, choices=STATUS_ITEMS, verbose_name="状态")
    in_nav = models.BooleanField(default=False, verbose_name="是否为导航")
    owner = models.ForeignKey(User, verbose_name="作者", on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    class Meta:
        verbose_name = verbose_name_plural = '分类'


class Tag(CreatedTime):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        (STATUS_DELETE, "删除"),
        (STATUS_NORMAL, "正常")
    )

    name = models.CharField(max_length=15,  verbose_name="标签名称")
    status = models.PositiveBigIntegerField(default=STATUS_NORMAL, choices=STATUS_ITEMS, verbose_name="状态")
    owner = models.ForeignKey(User, verbose_name="作者", on_delete=models.CASCADE)

    class Meta:
        verbose_name = verbose_name_plural = '标签'


class Article(CreatedTime):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_DRAFT = 2
    STATUS_ITEMS = (
        (STATUS_DRAFT, "草稿"),
        (STATUS_NORMAL, "正常"),
        (STATUS_DELETE, "删除")
    )

    title = models.CharField(max_length=255, verbose_name="标题")
    desc = models.CharField(max_length=1024, blank=True, verbose_name="摘要")
    content = models.TextField(verbose_name="正文", help_text="MarkDown格式")
    status = models.PositiveBigIntegerField(default=STATUS_DRAFT, choices=STATUS_ITEMS, verbose_name="状态")
    tag = models.ManyToManyField(Tag, verbose_name="标签", blank=True)
    owner = models.ForeignKey(User, verbose_name="作者", on_delete=models.CASCADE)
    # 表示外键关联到分类表,当作者表删除了该条数据,表中不删除,仅仅是把外键置空
    category = models.ForeignKey(Category, verbose_name="分类", null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = verbose_name_plural = '文章'
        ordering = ['-id']


