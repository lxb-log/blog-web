# -*- coding: utf-8 -*-
# Time: 2021/4/13 23:03

"""
Django settings for webserver project.

Generated by 'django-admin startproject' using Django 3.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-f4gui6u3)*)0bz9$-^0q^&mr_2tbf97)bmo$+5s+)7w4tci2-4'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'corsheaders', # 解决跨域

    'blog',
    'adminServer', # 后台管理
    'users',
]


# 指定本项目用户模型类:
AUTH_USER_MODEL = 'users.User'

# CORS跨域请求设置
CORS_ORIGIN_WHITELIST = (
    # 备注：允许源地址`http://127.0.0.1:8000`向当前API服务器发起跨域请求
    'http://127.0.0.1:8000',
    'http://localhost:8000',
)

CORS_ALLOW_CREDENTIALS = True  # 允许携带cookie


MIDDLEWARE = [
    # 注意：此中间件添加到中间件的第一个(CORS 跨域)
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'users.middleware.DIYAuthenticatedMiddlewareMixin'
]

ROOT_URLCONF = 'webserver.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # 添加这一行的配置信息, 把 templates的绝对路径导入到 [] 中
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'webserver.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # 数据库引擎
        'HOST': '121.41.206.74',  # 数据库主机
        'PORT': 3306,  # 数据库端口
        'USER': 'djangoblog',  # 数据库用户名
        'PASSWORD': 'Nishishui_0710',  # 数据库用户密码
        'NAME': 'blogserver'  # 数据库名字
    }, }



# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/
# 配置中文与时区
LANGUAGE_CODE = "zh-hans"
TIME_ZONE = "Asia/Shanghai"


USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# 指定自定义的用户认证后端:
AUTHENTICATION_BACKENDS = ['users.utils.UsernameEmailAuthBackend']

