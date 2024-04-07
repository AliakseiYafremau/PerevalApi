# Generated by Django 5.0.4 on 2024-04-07 13:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_alter_pereval_cords_alter_pereval_level'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('fam', models.CharField(max_length=25)),
                ('name', models.CharField(max_length=25)),
                ('otc', models.CharField(max_length=25)),
                ('phone', models.CharField(blank=True, max_length=17, null=True)),
            ],
        ),
        migrations.RenameModel(
            old_name='Pereval',
            new_name='PerevalAdded',
        ),
        migrations.AlterField(
            model_name='perevaladded',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.user'),
        ),
    ]
