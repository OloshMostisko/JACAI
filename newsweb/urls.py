from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.home, name='home' ),
    path('articleDetails/', views.articleDetailsView, name='articleDetailsView'),
    path('published-articles', views.pub_articles, name='pub_articles')
]