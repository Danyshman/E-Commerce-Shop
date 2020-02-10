from django.db import models
from django.conf import settings
from constants import *


def upload_ticket_image(instance, filename):
    filename = 'avatar.'+filename.split('.')[1]
    return "{user}/tickets/{subject}{filename}".format(user=instance,subject=instance.subject, filename=filename)


class SupportTicket(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, null=True, related_name='support_tickets')
    subject = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=255, choices=SUPPORT_TICKET_STATUS, null=True, blank=True,
                              default=SUPPORT_TICKET_STATUS[1])
    type = models.CharField(max_length=255, choices=SUPPORT_TICKET_TYPE, null=True, blank=True)
    priority = models.CharField(max_length=255, choices=SUPPORT_TICKET_PRIORITY, null=True, blank=True)
    description = models.TextField(max_length=2048, blank=True, null=True)
    img = models.ImageField(upload_to=upload_ticket_image, null=True, blank=True)
    date_submitted = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)

    def __str__(self):
        return str(self.subject)

