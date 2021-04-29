from django.shortcuts import render
from django.http import HttpResponse
from .models import Posts

# Create your views here.
#passing data into the template we use context

def home(request):
    return render(request,'blog/home.html')
def about(request):
    context={'title': 'About us'}
    return render(request, 'blog/about.html', context)

def login(request):
    context = {'title': 'Login '}
    return render(request, 'blog/logn.html')

def products(request):
    context = {'title': 'Products'}
    return render(request, 'blog/products.html')
