from django.shortcuts import render
from django.views.generic import DeleteView, ListView

from .models import About, Archive, Article, IndexPage, InformationPage, ClientContact


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

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contact'] = ClientContact.objects.all()
        return context


class AboutView(ListView):
    model = About
    template_name = 'about.html'
    context_object_name = 'about_page'
    extra_context = {'title': 'about'}


class ArchiveView(ListView):
    model = Archive
    queryset = Archive.objects.select_related('article').all()
    template_name = 'archive.html'
    context_object_name = 'archive_page'
    extra_context = {'title': 'archive'}


class ArticleDetailView(DeleteView):
    model = Article
    template_name = 'article_detail.html'
    slug_field = 'id'
    context_object_name = 'article_page'
    extra_context = {'title': 'article_detail'}
