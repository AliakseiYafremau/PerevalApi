# Generated by Django 5.0.4 on 2024-04-07 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_pereval_connect'),
    ]

    operations = [
        migrations.AddField(
            model_name='pereval',
            name='status',
            field=models.CharField(choices=[('new', 'новый'), ('pending', 'в работе'), ('accepted', 'принят'), ('rejected', 'отклонен')], default='new', max_length=50),
        ),
    ]