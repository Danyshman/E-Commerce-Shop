from django.db import models
import uuid
from constants import ORDER_STATUS
from django.conf import settings
from product.models import Product


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, null=True, related_name='orders')
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    status = models.CharField(max_length=255, choices=ORDER_STATUS, null=False, default='In Progress')
    products = models.ManyToManyField(Product)
    total_price = models.PositiveIntegerField(blank=True, null=True)
    date_purchased = models.DateField(auto_now_add=True)

