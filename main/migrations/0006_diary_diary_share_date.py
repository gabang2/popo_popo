# Generated by Django 4.0.4 on 2022-05-26 04:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20220524_2358'),
    ]

    operations = [
        migrations.AddField(
            model_name='diary',
            name='diary_share_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]