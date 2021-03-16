# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Chemistry(models.Model):
    cid = models.IntegerField(primary_key=True)
    structure = models.CharField(max_length=255, blank=True, null=True)
    molecularformula = models.CharField(db_column='MolecularFormula', max_length=255, blank=True, null=True)  # Field name made lowercase.
    molecularweight = models.CharField(db_column='MolecularWeight', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        
        db_table = 'chemistry'


class CodeImages(models.Model):
    code_images = models.CharField(primary_key=True, max_length=255)
    entryname = models.CharField(max_length=255, blank=True, null=True)
    compoundformula = models.CharField(max_length=255, blank=True, null=True)
    cid_id = models.CharField(max_length=255, blank=True, null=True)
    cid = models.IntegerField(blank=True, null=True)

    class Meta:
        
        db_table = 'code_images'

class Resource(models.Model):
    title = models.CharField(max_length=100)
    file = models.CharField(max_length=200)
    name = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'resource'

class Test(models.Model):
    name = models.CharField(primary_key=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'test'


