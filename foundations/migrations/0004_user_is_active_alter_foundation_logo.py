# Generated by Django 5.1.1 on 2024-09-27 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foundations', '0003_remove_users_id_couple_alter_typesdocument_desc_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=1, verbose_name='active'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='foundation',
            name='logo',
            field=models.ImageField(upload_to='media/logos/'),
        ),
    ]
