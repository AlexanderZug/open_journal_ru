from django.shortcuts import render

from .models import IndexPage, InformationPage


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
