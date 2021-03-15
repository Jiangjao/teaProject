# Generated by Django 3.0 on 2021-03-15 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teafound', '0007_remove_codeimages_chem_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='codeimages',
            name='id',
        ),
        migrations.AddField(
            model_name='codeimages',
            name='chem_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='codeimages',
            name='code_images',
            field=models.CharField(max_length=255, primary_key=True, serialize=False),
        ),
    ]
