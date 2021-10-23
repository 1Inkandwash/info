#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
如果一个子应用有100个视图，路由都写在工程的urls里不便于管理
在子应用下创建urls分担
"""
from django.urls import path
from book.views import index
urlpatterns = [
    # path(路由,视图函数名)
    path('index/', index),
]