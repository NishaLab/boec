from django import db
from django.db import models
from django.contrib.auth.models import User, AbstractUser
from .enums import *


class User(AbstractUser):
    discriminator = models.CharField(db_column='Discriminator', max_length=255)  # Field name made lowercase.
    role = models.SmallIntegerField(
        null=False,
        blank=False,
        default=UserRole.CUSTOMER.value,
        choices=[
            (UserRole.CUSTOMER.value, UserRole.CUSTOMER.name),
            (UserRole.SALE.value, UserRole.SALE.name),
            (UserRole.INVENTORY.value, UserRole.INVENTORY.name)
        ]
    )
    address = models.CharField(db_column='address', max_length=100, default="")
    phone = models.CharField(db_column='phone', max_length=100, default="")
    status = models.CharField(db_column='status', max_length=100, default="Available")

class Vendor(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=255, blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=255, blank=True, null=True)  # Field name made lowercase.
    desc = models.CharField(db_column='Desc', max_length=255, blank=True, null=True)  # Field name made lowercase.
class Category(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    desc = models.CharField(db_column='Desc', max_length=255, blank=True, null=True)  # Field name made lowercase.

class SubCategory(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    desc = models.CharField(db_column='Desc', max_length=255, blank=True, null=True)  # Field name made lowercase.
    parent = models.ForeignKey('Category', models.CASCADE, db_column='CategoryId')  # Field name made lowercase.
    
class Product(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    desc = models.CharField(db_column='Desc', max_length=255, blank=True, null=True)  # Field name made lowercase.
    category = models.ForeignKey('Category', models.CASCADE, db_column='CategoryId')  # Field name made lowercase.
class ProductVariant(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    product = models.ForeignKey('Product', models.CASCADE, db_column='ProductId')
    quantity = models.IntegerField(default=0)
    price = models.FloatField(db_column='Price')  # Field name made lowercase.\
    vendor = models.ForeignKey('Vendor', models.CASCADE, db_column='VendorId')
class OrderedProduct(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    quantity = models.IntegerField(default=0)
    price = models.FloatField(db_column='Price')  # Field name made lowercase.\
    product = models.ForeignKey('ProductVariant', models.CASCADE, db_column='VariantId')
    order = models.ForeignKey('Order', models.CASCADE, db_column='OrderId')
class Order(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    shipping_address = models.CharField(db_column='ShippingAddress', max_length=255, blank=True, null=True)
    customer = models.ForeignKey('User', models.CASCADE, related_name="customer", db_column='UserID')
    sale = models.ForeignKey('User', models.CASCADE,related_name="sale", db_column='SellerID', null=True)
    payment_type =  models.CharField(db_column='Payment_type', max_length=255, blank=True, null=True)
    create_at = models.DateTimeField(db_column="create_at", auto_now=True)
class ShippingInfo(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    status = models.IntegerField(default=0)
    create_at = models.DateTimeField(db_column="create_at", auto_now=True)
