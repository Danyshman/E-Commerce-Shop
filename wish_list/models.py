from django.db import models
from product.models import Product
from django.conf import settings
from django.contrib.postgres.fields import ArrayField


class WishList(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    products = ArrayField(models.CharField(max_length=512, null=True, blank=True))

    def get_products(self):
        ids = self.products
        items = []
        for id in ids:
            try:
                items.append(Product.objects.get(id=id))
            except Exception:
                self.products.remove(id)
        return items

    def add_product(self, product_id):
        try:
            item = Product.objects.get(id=product_id)
            self.products.append(product_id)
        except Exception:
            return 'Product with id {} does not exiest'.format(product_id)

    def remove_product(self, product_id):
        try:
            self.products.remove(product_id)
        except Exception:
            return 'Product with id {} does not exiest'.format(product_id)


