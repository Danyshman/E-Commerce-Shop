from django.db import models
import uuid
from constants import ORDER_STATUS
from account.models import User


class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date_purchased = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=255, choices=ORDER_STATUS, null=False, default='In Progress')
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='orders', null=True)
    total_price = models.PositiveIntegerField(blank=True, null=True)

