import random

from django.shortcuts import render, get_object_or_404

from .forms import MineralForm
from .models import Mineral


def mineral_detail(request, mineral_id):
    mineral = get_object_or_404(Mineral, pk=mineral_id)

    mineral_form = MineralForm(instance=mineral)

    all_mineral_count = Mineral.objects.all().count()
    rand_num = random.randint(1, all_mineral_count)

    context = {
        'mineral': mineral,
        'mineral_form': mineral_form,
        'rand_mineral': rand_num,
    }

    return render(request, 'detail.html', context)
