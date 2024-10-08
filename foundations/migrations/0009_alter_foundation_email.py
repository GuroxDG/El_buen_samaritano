# Generated by Django 5.1.1 on 2024-09-28 05:36

import foundations.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foundations', '0008_alter_donation_donation_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foundation',
            name='email',
            field=models.EmailField(max_length=254, unique=True, validators=[foundations.models.validate_email], verbose_name='correo'),
        ),
    ]
