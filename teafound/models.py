# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Chemistry(models.Model):
    cid = models.IntegerField(blank=True, null=True,unique=True)
    structure = models.CharField(max_length=255, blank=True, null=True)
    molecularformula = models.CharField(primary_key=True, max_length=255)
    molecularweight = models.CharField(max_length=255, blank=True, null=True)
    extra_word = models.TextField(blank=True, null=True)
    cas = models.CharField(db_column='CAS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    pubchem = models.CharField(db_column='PubChem', max_length=255, blank=True, null=True)  # Field name made lowercase.
    einecs = models.CharField(db_column='EINECS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    # entryname = models.CharField(max_length=255, blank=True, null=True)
    entryname = models.ImageField(upload_to='images/',verbose_name="pictureUsedNext", blank=True, null=True)
    
    class Meta:
        db_table = 'chemistry'

    def __str__(self):
        return self.molecularformula


class CodeImages(models.Model):
    code_images = models.CharField(primary_key=True, max_length=255)
    entryname = models.CharField(max_length=255, blank=True, null=True)
    compoundformula = models.CharField(max_length=255, blank=True, null=True)
    einecs = models.CharField(db_column='EINECS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cid = models.IntegerField(blank=True, null=True)
    extraword = models.TextField(db_column='extraWord', blank=True, null=True)  # Field name made lowercase.
    chinese_name = models.CharField(db_column='Chinese_name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    mocular_weight = models.FloatField(db_column='mocular weight', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    cas = models.CharField(db_column='CAS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cid_id = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'code_images'


class Resource(models.Model):
    title = models.CharField(max_length=100)
    file = models.CharField(max_length=200)
    name = models.CharField(max_length=200)

    class Meta:

        db_table = 'resource'

class Test(models.Model):
    name = models.CharField(primary_key=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'test'


