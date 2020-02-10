from django.shortcuts import render





















def index(request):
    return render(request, 'index.html')


def shop_page(request):
    return render(request, 'product/shop-grid.html')


def about_us(request):
    return render(request, 'about_us.html')


def contacts(request):
    return render(request, 'contacts.html')
