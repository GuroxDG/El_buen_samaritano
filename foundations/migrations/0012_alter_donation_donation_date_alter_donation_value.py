# Generated by Django 5.1.1 on 2024-09-28 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foundations', '0011_alter_user_document'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation',
            name='donation_date',
            field=models.DateField(auto_now_add=True, verbose_name='Fecha Donación'),
        ),
        migrations.AlterField(
            model_name='donation',
            name='value',
            field=models.DecimalField(decimal_places=2, max_digits=200),
        ),
    ]