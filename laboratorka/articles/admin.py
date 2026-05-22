from django.contrib import admin
from .models import Article


class ArticleAdmin(admin.ModelAdmin):
    exclude = ('slug',)

admin.site.register(Article, ArticleAdmin)