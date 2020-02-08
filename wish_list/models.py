from django.db import models
from product.models import Product
from account.models import User


class WishList(models.Model):
    # user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    products = models.ManyToManyField(Product)


