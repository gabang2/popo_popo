# Generated by Django 3.2.13 on 2022-06-06 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_user_user_signup_completed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_profile',
            field=models.ImageField(blank=True, default='default_img/diary_default_img.png', null=True, upload_to='profile_img/'),
        ),
    ]
