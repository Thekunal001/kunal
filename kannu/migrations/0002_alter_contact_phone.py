# Generated by Django 4.0.4 on 2022-06-12 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kannu', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.IntegerField(),
        ),
    ]
