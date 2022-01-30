from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404 , redirect
from django.views import generic
from .models import *
from django.conf import settings

# Create your views here.
# def home(request):
#     import requests
#     import json
#     api_request = requests.get("http://newsapi.org/v2/top-headlines?sources=google-news-in&apiKey=b910d1f00d0f4f4b8a4be92cbdb6bb50")
#     api = json.loads(api_request.content)
#     return render(request, 'home.html', {'api' : api})

def home(request):
    articles = PublishedArticles.objects.all()
    print(articles)
    context = {
       'articles': articles

    }
  
    return render(request, 'home.html',context)

def pub_articles(request):
    posts = PublishedArticles.objects.all()

    return render(request, 'home.html',{'posts' : posts.order_by('-publish_on')})
def articleDetailsView(request):
    
    #posts = PublishedArticles.objects.get(pk=post_id)
    
    return render(request, 'articleDetails.html')
