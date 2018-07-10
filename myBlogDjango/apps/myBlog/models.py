from datetime import datetime

from django.db import models

# Create your models here.
class BlogModel(models.Model):

    author = models.CharField(max_length=50,default="多个领域",verbose_name="作者")
    title = models.CharField(max_length=100,default="",verbose_name="标题")
    identify = models.CharField(max_length=200,default="",verbose_name="MD5")
    category = models.CharField(max_length=100,default="",verbose_name="分类")
    digest = models.CharField(max_length=200,default="",verbose_name="摘要")
    body = models.TextField(default="",verbose_name="文章内容")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "博客"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

