from django.urls import path,register_converter,re_path
from django.conf.urls import include,url
from . import views, converters
from .views import MySearchView

# 自定义过滤器
# register_converter(converters.IntConverter,'myint')
# register_converter(converters.FourDigitYearConverter, 'yyyy')

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('tables/', views.show_all_heros, name='tables'),
    path('showimages/', views.show_some_images, name='images'),
    path('download/', views.download, name='download'),
    path('about/', views.about, name='about'),
    # 这里为啥无法删除？？
    
    # path('search/', include('haystack.urls')),
    # ### 正则匹配
    # re_path('(?P<year>[0-9]{4}).html', views.myyear, name='urlyear'),

    # 路由分发
    path("tables/<int:cid>/",views.chemDetail, name="chemDetail"),
    # url(r'^search/$', views.search, name='search'),
    # url(r'^search/',include('haystack.urls'),name='search'),
    # 
    # path('search/',  MySearchView.as_view(), name='search_view'),

    # ### 自定义过滤器
    # path('<yyyy:year>', views.year), 
]