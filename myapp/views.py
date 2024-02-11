from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import web
from django.urls import reverse


def index(request):
    return render(request, 'first_page.html')


def dataset(request):
    data = web.objects.all().values()
    return render(request, 'dataset.html', {'data': data})


def insert(request):
    return render(request, 'insert.html')


def add(request):
    x = request.POST['name']
    y = request.POST['number']
    data = web(name=x, number=y)
    data.save()
    return HttpResponseRedirect(reverse('dataset'))


def delete(request, id):
    data = web.objects.get(id=id)
    data.delete()
    return HttpResponseRedirect(reverse('dataset'))


def retrieve(request, id):
    data = web.objects.get(id=id)
    return render(request, 'update.html', {'data': data})


def update(request, id):
    if request.method == 'POST':
        name = request.POST.get('name')
        number = request.POST.get('number')
        data = web.objects.filter(id=id)
        data.update(
            name=name,
            number=number
        )
        # data.name = name
        # data.number = number
        # data.save()
    return HttpResponseRedirect(reverse('dataset'))
