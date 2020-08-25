from collections import Counter
from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render_to_response


# Для отладки механизма ab-тестирования используйте эти счетчики
# в качестве хранилища количества показов и количества переходов.
# но помните, что в реальных проектах так не стоит делать
# так как при перезапуске приложения они обнулятся
counter_show = Counter()
counter_click = Counter()



def index(request):
    # Реализуйте логику подсчета количества переходов с лендига по GET параметру from-landing
    click = []
    count = request.GET.get('from-landing')
    if count == 'original':
        click = ['original']
        for name in click:
            counter_click[name] += 1

        
    elif count == 'test':
        click = ['test']
        for name in click:
            counter_click[name] += 1

    return render_to_response('index.html')


def landing(request):
    # Реализуйте дополнительное отображение по шаблону app/landing_alternate.html
    # в зависимости от GET параметра ab-test-arg
    # который может принимать значения original и test
    # Так же реализуйте логику подсчета количества показов
    name = request.GET.get('ab-test-arg')

    if name == 'original':
        show = ['original']
        for name in show:
            counter_show[name] += 1
        return render_to_response('landing.html')

    elif name == 'test':
        show = ['test']
        for name in show:
            counter_show[name] += 1
        return render_to_response('landing_alternate.html')
    else:
        raise Http404
    




def stats(request):
    # Реализуйте логику подсчета отношения количества переходов к количеству показов страницы
    # Чтобы отличить с какой версии лендинга был переход
    # проверяйте GET параметр marker который может принимать значения test и original
    # Для вывода результат передайте в следующем формате:
    if counter_click['original'] == 0 and counter_show['original'] == 0:
        res1 = 0
    elif counter_click['original'] == 0 :
        res1 = counter_show['original']
    elif counter_show['original'] == 0:
        res1 = counter_click['original']
    else:
        res1 = counter_click['original'] / counter_show['original']


    if counter_click['test'] == 0 and counter_show['test'] == 0:
        res2 = 0
    elif counter_click['test'] == 0 :
        res2 = counter_show['test']
    elif counter_show['test'] == 0:
        res2 = counter_click['test']
    else:
        res2 = counter_click['test'] / counter_show['test']
    return render_to_response('stats.html', context={
        'test_conversion': round(res2, 1),
        'original_conversion': round(res1, 1),
    })
