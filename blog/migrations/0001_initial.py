# Generated by Django 3.0.2 on 2020-01-28 17:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, max_length=2048, null=True)),
                ('category', models.CharField(choices=[], max_length=255)),
                ('main_img', models.ImageField(blank=True, null=True, upload_to='')),
                ('img2', models.ImageField(blank=True, null=True, upload_to='')),
                ('img3', models.ImageField(blank=True, null=True, upload_to='')),
                ('timestamp', models.DateField(auto_now_add=True)),
                ('last_updated', models.DateField(auto_now=True)),
                ('tags', models.CharField(blank=True, max_length=1024, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
