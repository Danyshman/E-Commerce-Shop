from django.shortcuts import render, get_object_or_404, reverse
from django.contrib.auth.decorators import login_required
from apps.product.models import Product
from apps.account.models import User
from django.http import HttpResponse, HttpResponseRedirect
import json


@login_required
def wishlist(request, product_id):
    if request.method == 'POST' and request.is_ajax():
        user = request.user
        product = get_object_or_404(Product, id=product_id)
        if product.user_set.filter(id=user.id):
            product.user_set.remove(user)
            data = {'message': 'product removed from wishlist successfully'}
            return HttpResponse(data, content_type='application/json')
        else:
            user.wishlist.add(get_object_or_404(Product, id=product_id))
            data = {'message': 'product added to wishlist successfully'}
            return HttpResponse(data, content_type='application/json')






















def index(request):
    return render(request, 'index.html')


def shop_page(request):
    return render(request, 'product/shop-grid.html')


def about_us(request):
    return render(request, 'about_us.html')


def contacts(request):
    return render(request, 'contacts.html')
