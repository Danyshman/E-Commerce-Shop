# Generated by Django 3.0.2 on 2020-02-08 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_remove_product_order'),
        ('order', '0002_auto_20200205_0446'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='products',
            field=models.ManyToManyField(to='product.Product'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('progress', 'In Progress'), ('canceled', 'Canceled'), ('delayed', 'Delayed'), ('delivered', 'Delivered')], default='In Progress', max_length=255),
        ),
    ]