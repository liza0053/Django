from django.shortcuts import render
from datetime import datetime

def index_page(request):
    context = {
        "title": 'Курс "Промышленное программирование"',
        "name": 'Fishkina Elizaveta',
        'count_page': 3
    }
    return render(request, 'main/index.html', context)


def time_page(request):
    now = datetime.now()
    context = {
        "title": 'Курс "Промышленное программирование"',
        'current_date': now.strftime('%d.%m.%Y'),
        'current_time': now.strftime('%H:%M:%S'),
    }
    return render(request, 'main/time.html', context)

def calc_page(request):
    a = int(request.GET.get['a', 0])
    b = int(request.GET.get['b', 0])
    context = {
        "title": 'Курс "Промышленное программирование"',
        "a": a,
        "b": b,
        "sum": a + b,
    }
    return render(request, 'main/calc.html', context)