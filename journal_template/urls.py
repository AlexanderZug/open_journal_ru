from django.urls import path

from . import views

app_name = 'journal_template'

urlpatterns = [
    path('', views.index, name='index'),
    path('info_page/', views.information, name='info'),
]