# Generated by Django 3.0 on 2021-04-11 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teafound', '0004_auto_20210411_1314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chemistry',
            name='cid',
            field=models.IntegerField(blank=True, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='chemistry',
            name='entryname',
            field=models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='pictureUsedNext'),
        ),
    ]
