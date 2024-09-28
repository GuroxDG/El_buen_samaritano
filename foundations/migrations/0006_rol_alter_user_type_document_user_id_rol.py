# Generated by Django 5.1.1 on 2024-09-27 13:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foundations', '0005_donation_donation_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=50, verbose_name='nombre')),
                ('description', models.TextField(verbose_name='descripcion')),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='type_document',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='TipoDocumento', to='foundations.typesdocument'),
        ),
        migrations.AddField(
            model_name='user',
            name='id_rol',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='rol', to='foundations.rol'),
        ),
    ]