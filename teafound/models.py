# -*- coding: utf-8 -*-
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
import datetime

class Chemistry(models.Model):
    cid = models.IntegerField(blank=True, primary_key=True )
    structure = models.CharField(max_length=255 ,blank=True, null=True,default='seeyou')
    MolecularFormula = models.CharField(max_length=255 ,blank=True, null=True)
    # pubDate = models.DateTimeField(default=datetime.now(),verbose_name="ModifyCreateDate")
    MolecularWeight = models.CharField(max_length=255 ,blank=True, null=True)
    # cid = models.CharField()
    # cid = models.CharField()
    # cid = models.CharField()

    class Meta:
        # managed = False
        db_table = 'chemistry'

class CodeImages(models.Model):
    code_images = models.CharField(primary_key=True, max_length=255,default='12')
    cid = models.CharField(max_length=255, blank=True, null=False)
    # chem_id = models.ForeignKey(Chemistry,on_delete=models.CASCADE,default='null)
    entryname = models.CharField(max_length=255, blank=True, null=True)  # Field name made lowercase.
    compoundformula = models.CharField(max_length=255 ,blank=True, null=True)  # Field name made lowercase.

    class Meta:
        # managed = False
        db_table = 'code_images'





class Resource(models.Model):
    title = models.CharField(max_length=100)
    file = models.CharField(max_length=200)
    name = models.FileField(upload_to='resource/%Y/%m/%d/',verbose_name="下载地址", max_length=200)

    class Meta:
        # managed = False
        db_table = 'resource'


class Test(models.Model):
    name = models.CharField(primary_key=True, max_length=255)

    class Meta:
        # managed = False
        db_table = 'test'


class UserGender(models.Model):
    user_id = models.IntegerField(primary_key=True)
    user_name = models.CharField(max_length=255)
    user_gender = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user_gender'



















