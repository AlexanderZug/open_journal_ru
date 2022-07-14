from django.urls import path

from .views import (AboutView, ArchiveView, ArticleDetailView, IndexView,
                    InformationView)

app_name = 'journal_template'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('info_page/', InformationView.as_view(), name='info'),
    path('about/', AboutView.as_view(), name='about'),
    path('archive/', ArchiveView.as_view(), name='archive'),
    path('article_detail/<str:slug>/', ArticleDetailView.as_view(), name='article_detail'),
]
