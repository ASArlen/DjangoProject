"""DjangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
###细说Django urls.py urlpatterns
###参考：https://blog.csdn.net/lht_521/article/details/80580118
###django 中的render和render_to_response()
###参考：https://www.cnblogs.com/wangchaowei/p/6750512.html
'''

Created on 2022年6月24日

@author: QQ

DJango如何处理请求
-   用户在敲下你的网址并回车，生成请求；
-   请求传递到urls.py；Django去urlpatterns中匹配链接（Django会在匹配到的第一个就停下来）；
-   一旦匹配成功，Django便会给出相应的view页面（该页面可以为一个Python的函数，或者基于view（Django内置的）的类），也就是用户看到的页面；
-   若匹配失败，则出现错误的页面。

'''
from django.contrib import admin
from django.urls import path,include
from QQTest import views


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('interface/list/',views.interface_list),
    path('interface/add/',views.interface_add),
    path('interface/delete/',views.interface_delete),
    # path('interface/(?P<year>/[1-9][0-9]?/)/view/',views.interface_view)
    path('interface/<int:nid>/update/',views.interface_update),
    path('interface/models/form/classification/',views.interface_classification)
]
