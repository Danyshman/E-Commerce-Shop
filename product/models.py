from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=555)
    base_price = models.PositiveIntegerField()
    discount = models.IntegerField()
    main_img = models.ImageField()
    sub_img1 = models.ImageField()
    sub_img2 = models.ImageField()
    sub_img3 = models.ImageField()
    sub_img4 = models.ImageField()


class Clothes(Product):
    target_sex = models.CharField(max_length=2)
    sizes = models.CharField(max_length=255)
    is_available = models.BooleanField(default=True)
    in_stock = models.IntegerField()
    product_tags = models.CharField(max_length=255)





