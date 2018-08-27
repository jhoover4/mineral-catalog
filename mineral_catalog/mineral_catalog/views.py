import random
import string

from django.core.paginator import Paginator
from django.shortcuts import render

from mineral_detail.models import Mineral


def index(request):
    """
    Index view is used for showing and filtering minerals. Search box takes precedence over letter filtering.
    """
    search_box_query = request.GET.get('search-box', None)

    if search_box_query:
        all_minerals = Mineral.objects.filter(name__contains=search_box_query)
        searched_letter = None
    else:
        searched_letter = request.GET.get('q', 'a')
        all_minerals = Mineral.objects.filter(name__startswith=searched_letter)

    paginator = Paginator(all_minerals, 101)

    all_minerals2 = Mineral.objects.all()
    rand_num = random.randint(1, all_minerals2.count())

    page = request.GET.get('page')
    minerals = paginator.get_page(page)

    context = {
        'minerals': minerals,
        'rand_mineral': rand_num,
        'letters': string.ascii_lowercase,
        'searched_letter': searched_letter,
        'search_term': search_box_query
    }

    return render(request, 'index.html', context)
