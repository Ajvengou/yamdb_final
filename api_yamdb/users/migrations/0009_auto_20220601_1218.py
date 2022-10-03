# Generated by Django 2.2.16 on 2022-06-01 08:18

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_user_confirmation_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=150, unique=True, validators=[django.core.validators.RegexValidator(code='invalid_username', message='Username must be Alphanumeric', regex='^[\\w.@+-]+$')], verbose_name='User name'),
        ),
    ]