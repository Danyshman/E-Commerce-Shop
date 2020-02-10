from django.shortcuts import render
from .models import Order


def order_list(request, *args, **kwargs):
    if request.method == 'GET':
        if request.user.is_authenticated:
            orders = request.user.orders.all()
            context = {
                "orders": orders
            }
            return render(request, 'order/account-orders.html', context)
