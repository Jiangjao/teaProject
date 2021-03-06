# Generated by Django 3.0 on 2021-03-17 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teafound', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserGender',
        ),
        migrations.AlterModelOptions(
            name='resource',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='test',
            options={'managed': False},
        ),
        migrations.RenameField(
            model_name='chemistry',
            old_name='MolecularFormula',
            new_name='molecularformula',
        ),
        migrations.RenameField(
            model_name='chemistry',
            old_name='MolecularWeight',
            new_name='molecularweight',
        ),
        migrations.AddField(
            model_name='codeimages',
            name='cid_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='chemistry',
            name='cid',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='chemistry',
            name='molecularformula',
            field=models.CharField(blank=True, db_column='MolecularFormula', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='chemistry',
            name='molecularweight',
            field=models.CharField(blank=True, db_column='MolecularWeight', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='codeimages',
            name='cid',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
