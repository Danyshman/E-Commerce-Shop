# Generated by Django 3.0.2 on 2020-02-05 04:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
        ('account', '0003_user_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='orders',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='orders', to='order.Order'),
        ),
    ]