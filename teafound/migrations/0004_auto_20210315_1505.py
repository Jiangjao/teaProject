# Generated by Django 3.0 on 2021-03-15 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teafound', '0003_auto_20210315_1504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='codeimages',
            name='chem_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
