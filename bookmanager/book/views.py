from django.shortcuts import render

# Create your views here.  在这里创建你的视图
"""
视图
所谓的视图 其实就是Python函数
视图函数有2个要求:
    1.视图函数的第一个参数就是接收请求.
      这个请求其实就是 HttpRequest的类对象
    2.必须返回一个响应 HttpResponse
"""
# request
from django.http import HttpRequest
from django.http import HttpResponse


# 我们期望用户输入 http://127.0.0.1:8000/index/
# 来访问视图函数

def index(request):
    # return HttpResponse('OK')
    """
        render()渲染模板,
        render内有HttpResponse,不用担心没有写会造成什么
        request, template_name, context=None
        request           请求
        template_name     模板名字
        context=None
    1.context 理解为将视图中的数据传递给HTML(模板)
    2.HTML(模板)采用{{变量}}形式来展示数据
    """
    # 模拟数据查询
    context = {
        'name': '马上双十一 点击有惊喜'
    }
    return render(request, 'book/index.html', context=context)
