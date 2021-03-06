# Generated by Django 3.0 on 2021-04-11 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teafound', '0003_auto_20210330_1509'),
    ]

    operations = [
        migrations.AddField(
            model_name='chemistry',
            name='entryname',
            field=models.FileField(blank=True, null=True, upload_to='images/', verbose_name='pictureUsedNext'),
        ),
        migrations.AlterField(
            model_name='codeimages',
            name='cid',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='resource',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]
