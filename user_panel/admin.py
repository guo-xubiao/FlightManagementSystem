from django.contrib import admin
from .models import NewsArticle, UserProfile  # 确保导入 NewsArticle 模型

admin.site.register(NewsArticle)
admin.site.register(UserProfile)
