# Generated by Django 4.1.3 on 2022-11-04 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rename_firma_cliente_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='image',
            field=models.ImageField(help_text='Ingrese su firma', upload_to=''),
        ),
    ]
