# Generated by Django 5.1.3 on 2024-11-21 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicios', '0002_alter_servicio_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicio',
            name='imagen',
            field=models.ImageField(upload_to='servicios'),
        ),
    ]
