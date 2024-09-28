# Generated by Django 5.1.1 on 2024-09-28 07:09

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foundations', '0012_alter_donation_donation_date_alter_donation_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation',
            name='value',
            field=models.DecimalField(decimal_places=2, max_digits=20),
        ),
        migrations.AlterField(
            model_name='foundation',
            name='email',
            field=models.EmailField(max_length=254, validators=[django.core.validators.EmailValidator()], verbose_name='correo'),
        ),
    ]
