# Generated by Django 2.1 on 2018-12-05 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_auto_20181205_2056'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image_5',
        ),
        migrations.RemoveField(
            model_name='product',
            name='image_5_big',
        ),
        migrations.AddField(
            model_name='productcategory',
            name='slug',
            field=models.SlugField(default='category', max_length=255, verbose_name='Url катергории'),
        ),
    ]
