from django.db import models
from django.conf import settings


def upload_status_image(instance, filename):
    return "blog/{author}/{title}/{filename}".format(author=instance.author, title=instance.title, filename=filename)


class Blog(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=255, blank=True, null=True)
    body = models.TextField(max_length=2048, blank=True, null=True)
    main_img = models.ImageField(upload_to=upload_status_image, blank=True, null=True)
    img2 = models.ImageField(upload_to=upload_status_image, blank=True, null=True)
    img3 = models.ImageField(upload_to=upload_status_image, blank=True, null=True)
    timestamp = models.DateField(auto_now_add=True)
    last_updated = models.DateField(auto_now=True)
    tags = models.CharField(max_length=1024, blank=True, null=True)