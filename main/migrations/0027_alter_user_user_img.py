# Generated by Django 3.2.13 on 2022-06-07 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0026_alter_user_user_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_img',
            field=models.FileField(blank=True, null=True, upload_to='user_img/'),
        ),
    ]