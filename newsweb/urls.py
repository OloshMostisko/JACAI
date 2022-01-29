from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.home, name='home' ),
    path('articleDetails/<post_id>/', views.articleDetailsView, name='article-details'),
    path('published-articles', views.pub_articles, name='pub_articles')
]