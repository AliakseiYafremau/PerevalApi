# Generated by Django 5.0.4 on 2024-04-07 10:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_rename_coords_cords'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pereval',
            old_name='coords',
            new_name='cords',
        ),
    ]
