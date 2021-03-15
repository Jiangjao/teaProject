# -*- coding: utf-8 -*-
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class CodeImages(models.Model):
    code_images = models.CharField(primary_key=True, max_length=255)
    
    entryname = models.CharField(max_length=255, blank=True, null=True)  # Field name made lowercase.
    compoundformula = models.CharField(max_length=255 ,blank=True, null=True)  # Field name made lowercase.

    class Meta:
        # managed = False
        db_table = 'code_images'



class Heros(models.Model):
    name = models.CharField(max_length=255)
    hp_max = models.FloatField(blank=True, null=True)
    hp_growth = models.FloatField(blank=True, null=True)
    hp_start = models.FloatField(blank=True, null=True)
    mp_max = models.FloatField(blank=True, null=True)
    mp_growth = models.FloatField(blank=True, null=True)
    mp_start = models.FloatField(blank=True, null=True)
    attack_max = models.FloatField(blank=True, null=True)
    attack_growth = models.FloatField(blank=True, null=True)
    attack_start = models.FloatField(blank=True, null=True)
    defense_max = models.FloatField(blank=True, null=True)
    defense_growth = models.FloatField(blank=True, null=True)
    defense_start = models.FloatField(blank=True, null=True)
    hp_5s_max = models.FloatField(blank=True, null=True)
    hp_5s_growth = models.FloatField(blank=True, null=True)
    hp_5s_start = models.FloatField(blank=True, null=True)
    mp_5s_max = models.FloatField(blank=True, null=True)
    mp_5s_growth = models.FloatField(blank=True, null=True)
    mp_5s_start = models.FloatField(blank=True, null=True)
    attack_speed_max = models.FloatField(blank=True, null=True)
    attack_range = models.CharField(max_length=255, blank=True, null=True)
    role_main = models.CharField(max_length=255, blank=True, null=True)
    role_assist = models.CharField(max_length=255, blank=True, null=True)
    birthdate = models.DateField(blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'heros'


class HerosPlay(models.Model):
    hero_name = models.CharField(max_length=255, blank=True, null=True)
    game_id = models.IntegerField(blank=True, null=True)
    player_name = models.CharField(max_length=255, blank=True, null=True)
    kda_k = models.IntegerField(blank=True, null=True)
    kda_d = models.IntegerField(blank=True, null=True)
    kda_a = models.IntegerField(blank=True, null=True)
    money = models.IntegerField(blank=True, null=True)
    damage_input = models.IntegerField(blank=True, null=True)
    damage_output = models.IntegerField(blank=True, null=True)
    win = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'heros_play'
        unique_together = (('hero_name', 'game_id'),)


class HerosTemp(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'heros_temp'


class HerosWithIndex(models.Model):
    name = models.CharField(unique=True, max_length=255)
    hp_max = models.FloatField(blank=True, null=True)
    hp_growth = models.FloatField(blank=True, null=True)
    hp_start = models.FloatField(blank=True, null=True)
    mp_max = models.FloatField(blank=True, null=True)
    mp_growth = models.FloatField(blank=True, null=True)
    mp_start = models.FloatField(blank=True, null=True)
    attack_max = models.FloatField(blank=True, null=True)
    attack_growth = models.FloatField(blank=True, null=True)
    attack_start = models.FloatField(blank=True, null=True)
    defense_max = models.FloatField(blank=True, null=True)
    defense_growth = models.FloatField(blank=True, null=True)
    defense_start = models.FloatField(blank=True, null=True)
    hp_5s_max = models.FloatField(blank=True, null=True)
    hp_5s_growth = models.FloatField(blank=True, null=True)
    hp_5s_start = models.FloatField(blank=True, null=True)
    mp_5s_max = models.FloatField(blank=True, null=True)
    mp_5s_growth = models.FloatField(blank=True, null=True)
    mp_5s_start = models.FloatField(blank=True, null=True)
    attack_speed_max = models.FloatField(blank=True, null=True)
    attack_range = models.CharField(max_length=255, blank=True, null=True)
    role_main = models.CharField(max_length=255, blank=True, null=True)
    role_assist = models.CharField(max_length=255, blank=True, null=True)
    birthdate = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'heros_with_index'


class HerosWithoutIndex(models.Model):
    name = models.CharField(max_length=255)
    hp_max = models.FloatField(blank=True, null=True)
    hp_growth = models.FloatField(blank=True, null=True)
    hp_start = models.FloatField(blank=True, null=True)
    mp_max = models.FloatField(blank=True, null=True)
    mp_growth = models.FloatField(blank=True, null=True)
    mp_start = models.FloatField(blank=True, null=True)
    attack_max = models.FloatField(blank=True, null=True)
    attack_growth = models.FloatField(blank=True, null=True)
    attack_start = models.FloatField(blank=True, null=True)
    defense_max = models.FloatField(blank=True, null=True)
    defense_growth = models.FloatField(blank=True, null=True)
    defense_start = models.FloatField(blank=True, null=True)
    hp_5s_max = models.FloatField(blank=True, null=True)
    hp_5s_growth = models.FloatField(blank=True, null=True)
    hp_5s_start = models.FloatField(blank=True, null=True)
    mp_5s_max = models.FloatField(blank=True, null=True)
    mp_5s_growth = models.FloatField(blank=True, null=True)
    mp_5s_start = models.FloatField(blank=True, null=True)
    attack_speed_max = models.FloatField(blank=True, null=True)
    attack_range = models.CharField(max_length=255, blank=True, null=True)
    role_main = models.CharField(max_length=255, blank=True, null=True)
    role_assist = models.CharField(max_length=255, blank=True, null=True)
    birthdate = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'heros_without_index'


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



















