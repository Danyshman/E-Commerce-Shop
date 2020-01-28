from django.db import models
from django.conf import settings


class Blog(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(max_length=2048, blank=True, null=True)
    category = models.CharField(max_length=255, choices=())
    main_img = models.ImageField( blank=True, null=True)
    img2 = models.ImageField(blank=True, null=True)
    img3 = models.ImageField(blank=True, null=True)
    timestamp = models.DateField(auto_now_add=True)
    last_updated = models.DateField(auto_now=True)
    tags = models.CharField(max_length=1024, blank=True, null=True)