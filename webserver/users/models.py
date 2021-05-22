# -*- coding: utf-8 -*-
# Time: 2021/5/21 20:10

from django.db import models
from django.contrib.auth.models import AbstractUser

# 重写用户模型类, 继承自 AbstractUser
class User(AbstractUser):
    """自定义用户模型类"""

    # 增加 mobile 字段--暂时备用
    mobile = models.CharField(max_length=11, unique=True, verbose_name='手机号')
    # 用于记录邮箱是否激活, 默认为 False: 未激活
    email_active = models.BooleanField(default=False, verbose_name='邮箱验证状态')

    # 对当前表进行相关设置:
    class Meta:
        db_table = 'blog_users'
        verbose_name = '用户'
        verbose_name_plural = verbose_name

    # 在 str 魔法方法中, 返回用户名称
    def __str__(self):
        return self.username