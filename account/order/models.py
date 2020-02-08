from django.db import models
import uuid
from constants import ORDER_STATUS
from django.conf import settings


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    status = models.CharField(max_length=255, choices=ORDER_STATUS, null=False, default='In Progress')
    total_price = models.PositiveIntegerField(blank=True, null=True)
    date_purchased = models.DateField(auto_now_add=True)

