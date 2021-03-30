from django.db import models


class Chemistry(models.Model):
    cid = models.IntegerField(blank=True, null=True)
    structure = models.CharField(max_length=255, blank=True, null=True)
    molecularformula = models.CharField(primary_key=True, max_length=255)
    molecularweight = models.CharField(max_length=255, blank=True, null=True)
    extra_word = models.TextField(blank=True, null=True)
    cas = models.CharField(db_column='CAS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    pubchem = models.CharField(db_column='PubChem', max_length=255, blank=True, null=True)  # Field name made lowercase.
    einecs = models.CharField(db_column='EINECS', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'chemistry'


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
        managed = False
        db_table = 'code_images'


class Test(models.Model):
    name = models.CharField(primary_key=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'test'

