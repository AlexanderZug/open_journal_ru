from django.shortcuts import render

from .models import IndexPage


def index(request):
    index_list = IndexPage.objects.select_related().all()
    context = {
        'page_obj': index_list,
    }
    return render(request, 'index.html', context)
