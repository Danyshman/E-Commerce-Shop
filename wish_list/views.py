from django.shortcuts import render
from .models import WishList


def get_items(request, *args, **kwargs):
    items = WishList.products
    context = {
        "products": items
    }
    return render(request, 'wish_list/account-wishlist.html', context)
