
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView

from .forms import ClientContactForm
from .models import About, Archive, Article, IndexPage, InformationPage


class IndexView(ListView):
    model = IndexPage
    template_name = 'index.html'
    context_object_name = 'page_obj'
    extra_context = {'title': 'index'}


class InformationView(CreateView):
    form_class = ClientContactForm
    template_name = 'info.html'
    extra_context = {'title': 'info'}
    success_url = reverse_lazy('journal_template:index')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['info_page'] = InformationPage.objects.all()
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


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_detail.html'
    slug_field = 'id'
    context_object_name = 'article_page'
    extra_context = {'title': 'article_detail'}
