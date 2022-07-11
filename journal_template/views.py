from django.shortcuts import render

from .models import About, Archive, IndexPage, InformationPage, Article


def index(request):
    index_list = IndexPage.objects.select_related().all()
    context = {
        'page_obj': index_list,
    }
    return render(request, 'index.html', context)


def information(request):
    info_page = InformationPage.objects.select_related().all()
    context = {
        'info_page': info_page,
    }
    return render(request, 'info.html', context)


def about(request):
    about_page = About.objects.select_related().all()
    context = {
        'about_page': about_page,
    }
    return render(request, 'about.html', context)


def archive(request):
    archive_page = Archive.objects.select_related().all()
    context = {
        'archive_page': archive_page,
    }
    return render(request, 'archive.html', context)


def article(request):
    article_page = Article.objects.select_related().all()
    context = {
        'article_page': article_page,
    }
    return render(request, 'article.html', context)
