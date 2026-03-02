from django.shortcuts import render

from articles.models import Article


def article_list(request):
    return render(request, 'articles/article_list.html')

def article_item(request, article_id):
    articles = Article.objects.get(slug=slug)
    return render(request, 'articles/article_item.html', {'articles': articles})