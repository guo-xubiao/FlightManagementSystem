# user_panel/models.py
from django.contrib.auth.models import User
from django.db import models

class NewsArticle(models.Model):
    title = models.CharField(max_length=200)  # 文章标题
    content = models.TextField()  # 文章内容
    published_date = models.DateTimeField(auto_now_add=True)  # 发布时间

    class Meta:
        verbose_name = '航班新闻'
        verbose_name_plural = '航班新闻'

    def __str__(self):
        return self.title
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,)
    full_name = models.CharField(max_length=100,verbose_name="全名")
    phone_number = models.CharField(max_length=15,verbose_name="手机号")

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = '用户信息'

    def __str__(self):
        return self.user.username

