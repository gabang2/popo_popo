# Generated by Django 4.0.4 on 2022-06-06 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_user_user_signup_completed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qna',
            name='qna_img',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
