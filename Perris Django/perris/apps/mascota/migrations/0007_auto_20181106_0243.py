# Generated by Django 2.1 on 2018-11-06 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mascota', '0006_auto_20181106_0242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascota',
            name='Descripcion',
            field=models.TextField(null=True),
        ),
    ]
