from django.db import models
from django.utils.html import strip_tags

class Article(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True) #уникальный идентификатор для URL
    body = models.TextField()
    date = models.DateField(auto_now_add=True)
    thumbnail = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return self.title

    def snippet(self):
        #возвращает первые 50 символов текста + "..."
        return self.body[:50] + '...'