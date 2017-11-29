# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Customer(models.Model):
    cust_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=11)
    vip = models.IntegerField(db_column='VIP')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'customer'


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class Facts(models.Model):
    cust = models.ForeignKey(Customer, models.DO_NOTHING, primary_key=True)
    game = models.ForeignKey('Games', models.DO_NOTHING)
    sell_data_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'facts'
        unique_together = (('cust', 'game'),)


class Games(models.Model):
    game_id = models.IntegerField(primary_key=True)
    team1_name = models.CharField(max_length=20)
    team2_name = models.CharField(max_length=20)
    stadium = models.ForeignKey('Stadiums', models.DO_NOTHING)
    game_data_time = models.DateTimeField()
    ticket_price = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'games'


class Stadiums(models.Model):
    stadium_id = models.IntegerField(primary_key=True)
    stadium_name = models.CharField(max_length=20)
    adress = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=11)

    class Meta:
        managed = False
        db_table = 'stadiums'


