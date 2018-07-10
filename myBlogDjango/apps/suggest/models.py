from django.db import models

# Create your models here.
class SuggestModel(models.Model):

    SUGGEST_TYPE = {
        (1, '建议'),
        (2, '纠正'),
    }

    identity = models.CharField(default="",max_length=100,verbose_name="博客标识",help_text="博客标识")
    nickname = models.CharField(default="",max_length=100,verbose_name="昵称",help_text="昵称")
    suggestType = models.IntegerField(choices=SUGGEST_TYPE,default=1,verbose_name="建议类型",help_text="建议类型")
    suggestContent = models.TextField(default="",verbose_name='建议内容',help_text="建议内容")

    class Meta:
        verbose_name = "建议"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.identity