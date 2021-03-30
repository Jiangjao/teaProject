# Generated by Django 3.0 on 2021-03-30 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teafound', '0002_auto_20210317_1019'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='resource',
            options={},
        ),
        migrations.AddField(
            model_name='chemistry',
            name='cas',
            field=models.CharField(blank=True, db_column='CAS', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='chemistry',
            name='einecs',
            field=models.CharField(blank=True, db_column='EINECS', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='chemistry',
            name='extra_word',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='chemistry',
            name='pubchem',
            field=models.CharField(blank=True, db_column='PubChem', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='codeimages',
            name='cas',
            field=models.CharField(blank=True, db_column='CAS', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='codeimages',
            name='chinese_name',
            field=models.CharField(blank=True, db_column='Chinese_name', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='codeimages',
            name='einecs',
            field=models.CharField(blank=True, db_column='EINECS', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='codeimages',
            name='extraword',
            field=models.TextField(blank=True, db_column='extraWord', null=True),
        ),
        migrations.AddField(
            model_name='codeimages',
            name='mocular_weight',
            field=models.FloatField(blank=True, db_column='mocular weight', null=True),
        ),
        migrations.AlterField(
            model_name='chemistry',
            name='cid',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='chemistry',
            name='molecularformula',
            field=models.CharField(max_length=255, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='chemistry',
            name='molecularweight',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='codeimages',
            name='cid',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='codeimages',
            name='cid_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
