# Generated by Django 4.0.4 on 2022-06-09 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0038_ordercount_user_alter_ordercount_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='order_agree',
        ),
        migrations.RemoveField(
            model_name='order',
            name='order_delivery_fee',
        ),
        migrations.RemoveField(
            model_name='order',
            name='order_number',
        ),
        migrations.AddField(
            model_name='order',
            name='order_address',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
