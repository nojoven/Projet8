""" This is an auto-generated Django model module.
 I used the command  'python manage.py inspectdb > models.py'  in PowerShell
 PLEASE NOTE THAT THE MODEL IS NOT UTF-8 ENCODED.
 SO WHEN YOU'LL TRY TO START DJANGO YOU WILL GET THIS ERROR :  "source code string cannot contain null bytes"
 THIS IS HOW YOU WILL AVOID HEADACHES: YOU MUST ENCODE THE FILE in UTF-8. THEN SAVE IT.
 THEN 'PYTHON MANAGE.PY RUNSERVER' WILL WORK.
 I USED NOTEPAD++ TO ENCODE THIS FILE USING UTF-8.
 You'll have to do the following manually to clean this up:
   * Rearrange models' order
   * Make sure each model has one field with primary_key=True
   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
 Feel free to rename the models, but don't rename db_table values or field names. """

from django.db import models


class Categories(models.Model):
    idcategories = models.AutoField(db_column='idCategories', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'categories'


class Favorites(models.Model):
    favoriteid = models.AutoField(db_column='FavoriteID', primary_key=True)  # Field name made lowercase.
    productid = models.IntegerField(db_column='ProductID')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255)  # Field name made lowercase.
    nutrigrade = models.CharField(db_column='Nutrigrade', max_length=255)  # Field name made lowercase.
    stores = models.CharField(db_column='Stores', max_length=255)  # Field name made lowercase.
    brands = models.CharField(db_column='Brands', max_length=255)  # Field name made lowercase.
    category = models.CharField(db_column='Category', max_length=255)  # Field name made lowercase.
    quantity = models.CharField(db_column='Quantity', max_length=255)  # Field name made lowercase.
    replacedid = models.IntegerField(db_column='ReplacedID')  # Field name made lowercase.
    replacedarticle = models.CharField(db_column='ReplacedArticle', max_length=255)  # Field name made lowercase.
    replacednutrigrade = models.CharField(db_column='ReplacedNutrigrade', max_length=255)  # Field name made lowercase.
    userid = models.CharField(db_column='UserID', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'favorites'


class Products(models.Model):
    idproduct = models.AutoField(db_column='idProduct', primary_key=True)  # Field name made lowercase.
    productname = models.CharField(db_column='ProductName', max_length=255)  # Field name made lowercase.
    stores = models.CharField(db_column='Stores', max_length=255)  # Field name made lowercase.
    brands = models.CharField(db_column='Brands', max_length=255)  # Field name made lowercase.
    nutrigrade = models.CharField(db_column='Nutrigrade', max_length=255)  # Field name made lowercase.
    category = models.CharField(db_column='Category', max_length=255)  # Field name made lowercase.
    quantity = models.CharField(db_column='Quantity', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False 
        db_table = 'products'


class Users(models.Model):
    userid = models.AutoField(db_column='UserID', primary_key=True)  # Field name made lowercase.
    username = models.CharField(db_column='Username', max_length=255)  # Field name made lowercase.
    password = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'users'
