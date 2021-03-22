# -*- coding: utf-8 -*-
"""
Django settings for teafind project.

Generated by 'django-admin startproject' using Django 3.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '&si09(un@dj@9oc9w0z497w_e6ry710!)dk-x4(5p(inqcv&^b'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['42.193.172.132','127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'grappelli',
    # ##内置的后台管理系统?
    'django.contrib.admin',
    # ##内置的用户认证系统?
    'django.contrib.auth',
    # ##所有model元数据?
    'django.contrib.contenttypes',
    # ##会话，表示当前访问网站的用户身份
    'django.contrib.sessions',
    # ##消息提示
    'django.contrib.messages',
    # ##锦泰资源路径
    'django.contrib.staticfiles',

    # 搜索引擎
    'haystack',
    
    # my applications
    'teafound',

    # 分页机制
    'pure_pagination',
    # 样式美化
    

    
]

# ##中间件是request和response对象之间的钩子Hook
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'teafind.urls'

TEMPLATES = [
    {
        # 模板引擎
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # 设置模板路径
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        # 是否在App里查找模板文件?
        'APP_DIRS': True,
        # 用于RequestContext上下文的调用函数
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # 添加media组件
                'django.template.context_processors.media',
            ],
        },
    },
]

WSGI_APPLICATION = 'teafind.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

# export PATH=$PATH:/usr/local/mysql/bin
# OSError: mysql_config not found
# pip install mysqlclient
# pip install pymysql
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'sql_heros_data_master',  # 数据库名，先前创建的
        'USER': 'root',     # 用户名，可以自己创建用户
        'PASSWORD': 'Dj224768',  # 密码
        'HOST': 'localhost',  # mysql服务所在的主机ip
        'PORT': '3306',         # mysql服务端口
        # 'NAME': BASE_DIR / 'db.sqlite3',
    },
    # 生产环境有可能连接第二个数据?
    # 'db2':{
    #     'ENGINE': 'django.db.backends.mysql',
    #     'NAME': 'sql_heros_data_master',  # 数据库名，先前创建的
    #     'USER': 'root',     # 用户名，可以自己创建用户
    #     'PASSWORD': 'Dj224768',  # 密码
    #     'HOST': 'localhost',  # mysql服务所在的主机ip
    #     'PORT': '3307',         # mysql服务端口
    #     # 'NAME': BASE_DIR / 'db.sqlite3',
    # }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# 分页相关设置
PAGINATION_SETTINGS = {
    'PAGE_RANGE_DISPLAYED': 5,
    'MARGIN_PAGES_DISPLAYED': 2,

    'SHOW_FIRST_PAGE_WHEN_INVALID': True,
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
# STATICFILES_DIRS = (os.path.join(BASE_DIR,'static'), )
# STATIC_ROOT = posixpath.join(*(BASE_DIR.split(os.path.sep) + ['static']))
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
    # os.path.join(BASE_DIR, 'apps/message_form/static'),
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media')

# 搜索引擎
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'PATH': os.path.join(os.path.dirname(__file__), 'whoosh_index'),
    },
}

# 自动更新索引
HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'

