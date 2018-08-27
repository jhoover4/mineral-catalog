import random
import string

from django.core.paginator import Paginator
from django.shortcuts import render

from mineral_detail.models import Mineral


def index(request):
    searched_letter = request.GET.get('q', 'a')

    all_minerals = Mineral.objects.filter(name__startswith=searched_letter)
    paginator = Paginator(all_minerals, 101)

    rand_num = random.randint(1, all_minerals.count())

    page = request.GET.get('page')
    minerals = paginator.get_page(page)

    letters = string.ascii_lowercase

    context = {'minerals': minerals,
               'rand_mineral': rand_num,
               'letters': letters,
               'searched_letter': searched_letter}

    return render(request, 'index.html', context)
