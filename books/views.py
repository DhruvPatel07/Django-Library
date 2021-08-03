from .models import Books
from .forms import BooksForm
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect


# Create your views here.

def index(request):
    return render(request, 'books/index.html')


def home(request):
    form = BooksForm(request.GET or None)
    if form.is_valid():
        form.save()
    return render(request, 'books/home.html', {'form': form})


def show(request):
    books = Books.objects.all()
    return render(request, 'books/show.html',{'books':books})


def delete(request,id):
    form = Books.objects.get(id=id)
    form.delete()
    return HttpResponseRedirect('/')


def contact(request):
    return HttpResponse("we are at contact")


def login(request):
    return HttpResponse("we are at login")
