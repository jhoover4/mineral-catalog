import random
import string

from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render

from mineral_detail.models import Mineral, Group


def index(request):
    """
    Index view is used for showing and filtering minerals. Search box takes precedence over letter filtering.
    """

    filters = {}

    search_box_query = request.GET.get('search-box', None)
    group_search_query = request.GET.get('group', None)
    color_search_query = request.GET.get('color', None)
    letter_search_query = None
    search_term = None

    if search_box_query:
        filters['search_box_query'] = Q(name__icontains=search_box_query)
    if group_search_query:
        filters['group_search_query'] = Q(group__name=group_search_query)
    if color_search_query:
        filters['color_search_query'] = Q(color=color_search_query)

    filtered_minerals = Mineral.objects.filter(**filters)

    all_mineral_ids = Mineral.objects.all().values('id')
    rand_num = random.randint(1, all_mineral_ids.count())

    paginator = Paginator(filtered_minerals, 101)
    page = request.GET.get('page')
    minerals = paginator.get_page(page)

    groups = Group.objects.values('name').order_by('name')

    context = {
        'minerals': minerals,
        'rand_mineral': rand_num,
        'letters': string.ascii_lowercase,
        'searched_letter': letter_search_query,
        'search_term': search_term,
        'mineral_groups': groups
    }

    return render(request, 'index.html', context)
