from django.http import HttpResponse
from django.shortcuts import render

# views.py

from .models import Cat

def cat_index(request):
    cats = Cat.objects.all()
    return render(request, 'cats/index.html', {'cats': cats})

def cat_detail(request, cat_id):
    cat = Cat.objects.get(id=cat_id)
    return render(request, 'cats/detail.html', {'cat': cat})


# Define the home view function
def home(request):
    # Send a simple HTML response
    return HttpResponse('<h1>Hello ᓚᘏᗢ</h1>')

def about(request):
    return HttpResponse("<h1>About the CatCollector</h1>")

def about(request):
    return render(request, 'about.html')

def home(request):
    return render(request, 'home.html')


