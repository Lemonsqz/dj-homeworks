from django.shortcuts import render_to_response, redirect
from django.urls import reverse


import csv
from django.core.paginator import Paginator


def index(request):
    return redirect(reverse(bus_stations))


def bus_stations(request):
    with open('data-398-2018-08-30.csv', encoding='cp1251') as csvfile:
        data = list(csv.DictReader(csvfile, delimiter=','))

    paginator = Paginator(data, 10)
    current_page = request.GET.get('page', 1)
    all_obj = paginator.get_page(current_page)
    prev_page, next_page = None, None

    if all_obj.has_previous():
        prev_page = all_obj.previous_page_number()
    if all_obj.has_next():
        next_page = all_obj.next_page_number()

    return render_to_response('index.html', context={
        'bus_stations': all_obj,
        'current_page': current_page,
        'prev_page_url': prev_page,
        'next_page_url': next_page,
    })
