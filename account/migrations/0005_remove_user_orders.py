# Generated by Django 3.0.2 on 2020-02-05 04:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_user_orders'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='orders',
        ),
    ]
