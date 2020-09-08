from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView

from phones.models import Phone


def show_catalog(request):
    template = 'catalog.html'

    position = request.GET.get('sort')
    if position == 'name':
        phone = Phone.objects.all()
        context = {
            'phone1': phone[1],
            'phone2': phone[2],
            'phone3': phone[0],
        }
        return render(request, template, context)
    elif position == 'expensive':
        phone = Phone.objects.all()
        context = {
            'phone1': phone[1],
            'phone2': phone[0],
            'phone3': phone[2],
        }
        return render(request, template, context)
    elif position == 'cheap':
        phone = Phone.objects.all()
        context = {
            'phone1': phone[2],
            'phone2': phone[0],
            'phone3': phone[1],
        }
        return render(request, template, context)
    else:
        phone = Phone.objects.all()
        context = {
            'phone1': phone[0],
            'phone2': phone[1],
            'phone3': phone[2],

        }
        return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'

    test = Phone.objects.all()
    if slug == 'samsung-galaxy-edge-2':
        context = {
            'models': test[0],
        }
    elif slug == 'iphone-x':
        context = {
            'models': test[1],
        }
    elif slug == 'nokia-8':
        context = {
            'models': test[2],
        }
    return render(request, template, context)
