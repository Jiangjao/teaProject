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
