# Generated by Django 3.0.2 on 2020-02-08 17:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_auto_20200208_1749'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='final_price',
        ),
    ]
