"""yolov5Project URL Configuration

`urlpatterns` 列表将 URL 路由到视图。 有关更多信息，请参阅：
     https://docs.djangoproject.com/en/3.2/topics/http/urls/
例子：
函数视图
     1. 添加导入：from my_app 导入视图
     2.在urlpatterns中添加一个URL： path('', views.home, name='home')
基于类的视图
     1.添加导入：from other_app.views import Home
     2.在urlpatterns中添加一个URL：path('', Home.as_view(), name='home')
包括另一个 URLconf
     1.导入include()函数：from django.urls import include, path
     2.在urlpatterns中添加一个URL： path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from yolov5Project.controller import TestController

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', TestController.hello),
]
