from django.urls import path
from .views import ArticleCreateView, ArticleDetailView, ArticleListView

urlpatterns = [
    path('article/create/', ArticleCreateView.as_view(), name='article_new'),
    path('article/<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('', ArticleListView.as_view(), name='article_list'),
]
