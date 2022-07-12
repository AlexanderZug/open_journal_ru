from django.urls import path

from . import views
from .views import IndexView, InformationView, AboutView, ArchiveView, ArticleView, ArticleDetailView

app_name = 'journal_template'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('info_page/', InformationView.as_view(), name='info'),
    path('about/', AboutView.as_view(), name='about'),
    path('archive/', ArchiveView.as_view(), name='archive'),
    path('article/', ArticleView.as_view(), name='article'),
    path('article_detail/<str:slug>/', ArticleDetailView.as_view(), name='article_detail'),
]