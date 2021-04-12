# views.search

## django-haystack的版本要和Django的匹配

    不融洽的匹配，就得配置view
    修改一下搜索表单，让它提交数据到 django haystack 搜索视图对应的 URL：

-------

## router 冲突解决方案是：去除不必要的元素

    ```html

        <form role="search" method="get" id="searchform" action="{% url 'haystack_search' %}">
        <input type="search" name="q" placeholder="搜索" required>
        <button type="submit"><span class="ion-ios-search-strong"></span></button>
        </form>
    ```
    主要是把表单的 action 属性改为 {% url 'haystack_search' %}
    https://zhuanlan.zhihu.com/p/106763702

从8000端口到80端口，使用uwsgi和nginx 转发，提高了性能
后台运行uwsgi 
uwsgi -d --ini uwsgi.ini
8.启动项目
进入uwsgi.ini文件目录中：
新建uwsgi.ini 配置文件， 内容如下：
    
    # mysite_uwsgi.ini file
    [uwsgi]
    
    # Django-related settings
    # the base directory (full path)
    chdir           = /home/bobby/Projects/MxOnline
    # Django's wsgi file
    module          = MxOnline.wsgi
    # the virtualenv (full path)
    
    # process-related settings
    # master
    master          = true
    # maximum number of worker processes
    processes       = 10
    # the socket (use the full path to be safe
    socket          = 127.0.0.1:8000
    # ... with appropriate permissions - may be needed
    # chmod-socket    = 664
    # clear environment on exit
    vacuum          = true
    virtualenv = /home/bobby/.virtualenvs/mxonline
    
    logto = /tmp/mylog.log

注：
    chdir： 表示需要操作的目录，也就是项目的目录
    module： wsgi文件的路径
    processes： 进程数
    virtualenv：虚拟环境的目录
        

<!-- 查看端口.. -->
ps -ef | grep uwsgi

workon mxonline
uwsgi -i 你的目录/Mxonline/conf/uwsgi.ini &
uwsgi --ini uwsgi.ini
3.查看nginx的状态
systemctl status nginx 查看nginx的状态
system start/stop/enable/disable nginx 启动/关闭/设置开机启动/禁止开机启动
service nginx status/stop/restart/start 查看状态/停止/重启/开启 ngnix
安装完成后，如果不能启动nginx，可以使用 ps -ef | grep nginx 查看进程，杀掉全部的nginx进程，再重新启动nginx
 sudo /usr/sbin/nginx
作者：裴general
链接：https://www.jianshu.com/p/c060448b3e78
来源：简书
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
#	1. learn how to deploy on web

##	1.1 set permission  of nginx configuration  to root is available
##	1.2 please read the document of uwsgi and nginx


mysql修改表、字段、库的字符集(转)
原文链接：http://fatkun.com/2011/05/mysql-alter-charset.html

MySQL中默认字符集的设置有四级:服务器级，数据库级，表级 。最终是字段级 的字符集设置。注意前三种均为默认设置，并不代码你的字段最终会使用这个字符集设置。所以我们建议要用show create table table ; 或show full fields from tableName; 来检查当前表中字段的字符集设置。

 

修改数据库字符集：

 

ALTER DATABASE db_name DEFAULT CHARACTER SET character_name [COLLATE ...];
 

把表默认的字符集和所有字符列（CHAR,VARCHAR,TEXT）改为新的字符集：

 

ALTER TABLE tbl_name CONVERT TO CHARACTER SET character_name [COLLATE ...]
如：ALTER TABLE logtest CONVERT TO CHARACTER SET utf8 COLLATE utf8_general_ci;
 

只是修改表的默认字符集：

 

ALTER TABLE tbl_name DEFAULT CHARACTER SET character_name [COLLATE...];
如：ALTER TABLE logtest DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
 

修改字段的字符集：

 

ALTER TABLE tbl_name CHANGE c_name c_name CHARACTER SET character_name [COLLATE ...];
如：ALTER TABLE logtest CHANGE title title VARCHAR(100) CHARACTER SET utf8 COLLATE utf8_general_ci;
 

查看数据库编码：

 

SHOW CREATE DATABASE db_name;
 

查看表编码：

 

SHOW CREATE TABLE tbl_name;
 

查看字段编码：

 

SHOW FULL COLUMNS FROM tbl_name;