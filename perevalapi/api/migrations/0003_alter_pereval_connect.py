# Generated by Django 5.0.4 on 2024-04-07 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_coords_latitude_alter_coords_longitude'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pereval',
            name='connect',
            field=models.CharField(default='', max_length=20),
        ),
    ]
