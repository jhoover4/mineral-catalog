import random

from django.core.paginator import Paginator
from django.shortcuts import render


from mineral_detail.models import Mineral

# TODO: Make elements line up properly.

def index(request):
    all_minerals = Mineral.objects.all()
    paginator = Paginator(all_minerals, 101)

    rand_num = random.randint(1, all_minerals.count())

    page = request.GET.get('page')
    minerals = paginator.get_page(page)

    context = {'minerals': minerals,
               'rand_mineral': rand_num}

    return render(request, 'index.html', context)
