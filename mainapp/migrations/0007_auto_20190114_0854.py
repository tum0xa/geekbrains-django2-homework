# Generated by Django 2.1 on 2019-01-14 03:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0006_productcategory_is_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('city', models.CharField(max_length=50, verbose_name='Город')),
                ('street', models.CharField(max_length=50, verbose_name='Улица')),
                ('building', models.SmallIntegerField(verbose_name='Номер здания, дома')),
                ('office', models.SmallIntegerField(blank=True, verbose_name='Номер офиса')),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Название организации')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Имя')),
                ('number', models.CharField(blank=True, default='-', max_length=20, verbose_name='Номер телефона')),
                ('email', models.EmailField(blank=True, default='-', max_length=254, verbose_name='E-mail')),
                ('is_main', models.BooleanField(default=False, verbose_name='Основной')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Company')),
            ],
        ),
        migrations.AddField(
            model_name='address',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Company'),
        ),
    ]