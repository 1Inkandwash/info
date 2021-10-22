from django.db import models

# Create your models here.在这里创建模型
"""
1.我们的模型类  需要继承自  models.Model
2.系统会自动为我们添加一个主键--id
3.字段
    字段名=model.类型(选项)
    字段名其实就是数据表的字段名
    字段名不要使用python、mysql等关键字
    char(M)
    varchar(M)
    M 就是选项
"""


# ORM 类 对象 属性      DB 数据表  数据行  字段
# 一个类对应一个数据表  对象->数据行  属性 -> 字段
# 准备书籍列表信息的模型类
class BookInfo(models.Model):
    # 创建字段，字段类型...
    name = models.CharField(max_length=10)


# 准备人物列表信息的模型类(未理解)
class PeopleInfo(models.Model):
    name = models.CharField(max_length=10)
    gender = models.BooleanField()
    # 外键约束：人物属于哪本书
    # 外键要指定所属的模型类book = models.ForeignKey(BookInfo)
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE)

# makemigrations 生成数据库同步脚本
# migrations 迁移[网络释义:数据库迁移]
# no changes detected 没有检测到变化
