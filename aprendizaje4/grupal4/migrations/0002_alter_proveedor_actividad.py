# Generated by Django 4.2 on 2023-05-03 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grupal4', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proveedor',
            name='actividad',
            field=models.CharField(max_length=150),
        ),
    ]
