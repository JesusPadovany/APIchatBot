# Generated by Django 2.2.1 on 2019-05-09 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bender', '0002_product_productimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productimage',
            name='url',
        ),
        migrations.AddField(
            model_name='productimage',
            name='image',
            field=models.ImageField(default='false', upload_to='imagenes_producto'),
        ),
    ]
