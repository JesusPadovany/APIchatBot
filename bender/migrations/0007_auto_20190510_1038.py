# Generated by Django 2.2 on 2019-05-10 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bender', '0006_auto_20190509_2159'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('rol', models.CharField(max_length=200)),
                ('image', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='Reflection',
        ),
    ]
