from django.shortcuts import render
from .models import Book
from math import ceil

# Create your views here.
from django.http import HttpResponse

def index(request):
    books = Book.objects.all()
    print(books)
    n = len(books)
    nSlides = n // 4 + ceil((n / 4) - (n // 4))
    #params = {'no_of_slides': nSlides, 'range': range(1, nSlides), 'book': books}
    allBooks = [[books, range(1, nSlides), nSlides],
                [books, range(1, nSlides), nSlides]]
    params = {'allBooks':allBooks}
    return render(request, 'bookapp/index.html', params)


def about(request):
    return render(request, 'bookapp/about.html')

def contact(request):
    return HttpResponse("We are at contact")

def track(request):
    return HttpResponse("We are at tracker")

def search(request):
    return HttpResponse("We are at search")

def productView(request):
    return HttpResponse("We are at product view")

def checkout(request):
    return HttpResponse("We are at checkout")

