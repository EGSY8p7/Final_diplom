# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Airdata(models.Model):
    number = models.IntegerField(db_column='Number', blank=True, null=True)  # Field name made lowercase.
    datet = models.DateTimeField(db_column='DateT', blank=True, null=True)  # Field name made lowercase.
    pm25 = models.IntegerField(db_column='PM25', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'AirData'

