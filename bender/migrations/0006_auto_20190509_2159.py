# Generated by Django 2.2.1 on 2019-05-10 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bender', '0005_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.CharField(max_length=200),
        ),
        migrations.DeleteModel(
            name='ProductImage',
        ),
    ]
