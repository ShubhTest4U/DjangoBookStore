from django.shortcuts import render
from .models import Book, Contact, Orders
from math import ceil
import logging
# Get an instance of a logger
logger = logging.getLogger(__name__)
# Create your views here.
from django.http import HttpResponse

def index(request):
    #books = Book.objects.all()
    #print(books)
    #n = len(books)
    #nSlides = n // 4 + ceil((n / 4) - (n // 4))
    #params = {'no_of_slides': nSlides, 'range': range(1, nSlides), 'book': books}
    #allBooks = [[books, range(1, nSlides), nSlides],
                #[books, range(1, nSlides), nSlides]]

    allBooks = []
    catbooks = Book.objects.values('category', 'id')
    cats = {item['category'] for item in catbooks}
    for cat in cats:
        book = Book.objects.filter(category=cat)
        n = len(book)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allBooks.append([book, range(1, nSlides), nSlides])

    params = {'allBooks':allBooks}
    return render(request, 'bookapp/index.html', params)


def about(request):
    return render(request, 'bookapp/about.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()

    return render(request, 'bookapp/contact.html')

def track(request):
    return render(request, 'bookapp/track.html')

def search(request):
    return render(request, 'bookapp/search.html')

def productView(request, myid):
    # fetch books through id
    book = Book.objects.filter(id=myid)
    return render(request, 'bookapp/prodview.html', {'book':book[0]})

def checkout(request):
    if request.method == "POST":
        items_json = request.POST.get('itemsJson', '')
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address1', '') + " " + request.POST.get('address2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        phone = request.POST.get('phone', '')
        order = Orders(items_json=items_json, name=name, email=email, address=address, city=city,
                       state=state, zip_code=zip_code, phone=phone)
        order.save()
        thank = True
        id = order.order_id
        return render(request, 'bookapp/checkout.html', {'thank': thank, 'id': id})
    return render(request, 'bookapp/checkout.html')

