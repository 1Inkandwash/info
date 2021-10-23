from django.contrib import admin

# Register your models here.  在这里注册您的模型。
from book.models import BookInfo, PeopleInfo
# 注册模型类
admin.site.register(BookInfo)
admin.site.register(PeopleInfo)
# 注册完之后，要重新运行django
