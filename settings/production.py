import os
from .base import *

#从环境变量获取 SECRET_KEY，及其它敏感数据；
#容器化的环境下，这些数据保存在专用的 secret 存储，或者 KMS 系统中
#如 Kubernetes Secret中，云厂商的 KMS 服务，或者开源的 Vault 服务中

ALLOWED_HOSTS = ["127.0.0.1", "host.docker.internal","*"]

SECRET_KEY = '&si09(un@dj@9oc9w0z497w_e6ry710!)dk-x4(5p(inqcv&^b'

DEBUG = False

INSTALLED_APPS += (
    #'debug_toolbar', # and other apps for local development
)
