from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'books/index.html')

def login(request):
    return HttpResponse("we are at login")
