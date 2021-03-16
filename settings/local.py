from .base import *

DEBUG = True

ALLOWED_HOSTS = ["127.0.0.1"]

## 务必修改以下值，确保运行时系统安全:
SECRET_KEY = '&si09(un@dj@9oc9w0z497w_e6ry710!)dk-x4(5p(inqcv&^b'

## 如果仅使用数据库中的账号，以下 LDAP 配置可忽略
## 替换这里的配置为正确的域服务器配置，同时可能需要修改 base.py 中的 LDAP 服务器相关配置:
# LDAP_AUTH_URL = "ldap://xxxxx:389"
# LDAP_AUTH_CONNECTION_USERNAME = "admin"
# LDAP_AUTH_CONNECTION_PASSWORD = "your_admin_credentials"

INSTALLED_APPS += (
    # other apps for production site
)