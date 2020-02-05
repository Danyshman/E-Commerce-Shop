from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=555)
    base_price = models.PositiveIntegerField(default=0)
    discount = models.IntegerField(default=0)
    final_price = models.IntegerField(default=0)
    in_stock = models.IntegerField(default=1)
    main_img = models.ImageField(blank=True, null=True)
    sub_img1 = models.ImageField(blank=True, null=True)
    sub_img2 = models.ImageField(blank=True, null=True)
    sub_img3 = models.ImageField(blank=True, null=True)
    sub_img4 = models.ImageField(blank=True, null=True)


class Clothes(Product):
    target_sex = models.CharField(max_length=2, blank=True, null=True)
    sizes = models.CharField(max_length=255, blank=True, null=True)
    is_available = models.BooleanField(default=True)
    product_tags = models.CharField(max_length=255, blank=True, null=True)





