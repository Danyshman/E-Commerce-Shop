from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def shop_page(request):
    print('in view')
    return render(request, 'shop-grid.html')
