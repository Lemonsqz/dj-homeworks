from django.shortcuts import render
from phones.models import *

def show_catalog(request):
    template = 'catalog.html'
    phone1 = Phones.objects.get(id=1)
    phone2 = Phones.objects.get(id=2)
    sam = Samsung.objects.get(id=1)
    xia = Xiaomi.objects.get(id=1)
    context = {
        'options1': phone1,
        'options2': phone2,
        'sams': sam,
        'xiao': xia,
    }


    return render(
        request,
        template,
        context
    )

# создать условия и таблицу
