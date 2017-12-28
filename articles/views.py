from django.shortcuts import render
from .models import Article
from django.http import HttpResponse
from anaconda_navigator.utils.py3compat import request

def articles_list(request):
    articles = Article.objects.all().order_by('date')
    return render(request,"articles/articles_list.html",{'articles':articles})

def articles_details(request, slug):
    #return HttpResponse(slug)
    article = Article.objects.get(slug = slug)
    return render(request,"articles/article_details.html",{'article':article})

def articles_test(request):
    article =  Article.objects.all()
    return render(request,"articles.article_list.html") 
