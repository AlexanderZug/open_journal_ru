from django.shortcuts import render

from .models import About, Archive, IndexPage, InformationPage, Article
from django.views.generic import ListView


class IndexView(ListView):
    model = IndexPage
    template_name = 'index.html'
    context_object_name = 'page_obj'
    extra_context = {'title': 'index'}


class InformationView(ListView):
    model = InformationPage
    template_name = 'info.html'
    context_object_name = 'info_page'
    extra_context = {'title': 'info'}


class AboutView(ListView):
    model = About
    template_name = 'about.html'
    context_object_name = 'about_page'
    extra_context = {'title': 'about'}


class ArchiveView(ListView):
    model = Archive
    template_name = 'archive.html'
    context_object_name = 'archive_page'
    extra_context = {'title': 'archive'}


class ArticleView(ListView):
    model = Article
    template_name = 'article.html'
    context_object_name = 'article_page'
    extra_context = {'title': 'article'}


def article_detail(request, slug):
    article_detail = Article.objects.get(id=slug)
    context = {
        'article_detail': article_detail,
    }
    return render(request, 'article_detail.html', context)
