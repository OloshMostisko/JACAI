from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.home, name='home' ),
    path('articledetails', views.articleDetailsView, name='articledetails'),
    path('published-articles', views.pub_articles, name='pub_articles')
]