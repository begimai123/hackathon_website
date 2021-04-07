from django.shortcuts import render
from shop.models import Product
from django.db.models import Q

def searchResult(request):
    products = None
    query = request.GET.get('q')
    if query:
        products = Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
    return render(request, 'search.html', {'products':products})


