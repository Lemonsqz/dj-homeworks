from django.shortcuts import render
import csv

def inflation_view(request):
    template_name = 'inflation.html'

    path = 'inflation_russia.csv'
    file = open(path, encoding='utf-8', newline='')
    reader = list(csv.DictReader(file, delimiter=';'))
    # чтение csv-файла и заполнение контекста

    context = {
        'objects': reader,
    }

    return render(request, template_name,
                  context)