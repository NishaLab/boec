from django import db
from django.db import models
from django.contrib.auth.models import User, AbstractUser
from .enums import *
from django.db.models import Index
from django.db.models.functions.text import Lower


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
    email = models.CharField(db_column='email', max_length=100, default="")
    userlink = models.CharField(db_column='link', max_length=100, default="")

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
    sub_category = models.ForeignKey('SubCategory', models.CASCADE, db_column='SubCategoryId', null=True)

class ProductVariant(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    product = models.ForeignKey('Product', models.CASCADE, db_column='ProductId')
    quantity = models.IntegerField(default=0)
    price = models.FloatField(db_column='Price')  # Field name made lowercase.\
    vendor = models.ForeignKey('Vendor', models.CASCADE, db_column='VendorId')
    is_feature = models.BooleanField(db_column='is_feature', default=False)
    is_selling = models.BooleanField(db_column='is_selling', default=False)
    sale_off = models.FloatField(db_column='sale_off', default=0, null=True)
    brand = models.ForeignKey('Brand', models.CASCADE, db_column='BrandId',blank=True, null=True)
    publisher = models.ForeignKey('Publisher', models.CASCADE, db_column='PublisherId',blank=True, null=True)
    author = models.ForeignKey('Author', models.CASCADE, db_column='AuthorId',blank=True, null=True)
    designer = models.ForeignKey('Designer', models.CASCADE, db_column='DesignerId',blank=True, null=True)
class VariantOption(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    product = models.ForeignKey('ProductVariant', models.CASCADE, db_column='VariantId')
    quantity = models.IntegerField(default=0)
    price = models.FloatField(db_column='Price')  # Field name made lowercase.\
    name = models.CharField(db_column='name', max_length=255, blank=True, null=True)
class OrderedProduct(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    quantity = models.IntegerField(default=0)
    price = models.FloatField(db_column='Price')  # Field name made lowercase.\
    product = models.ForeignKey('VariantOption', models.CASCADE, db_column='OptionId')
    order = models.ForeignKey('Order', models.CASCADE, db_column='OrderId')

class Order(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    customer = models.ForeignKey('User', models.CASCADE, related_name="customer", db_column='UserID', blank=True, null=True)
    sale = models.ForeignKey('User', models.CASCADE,related_name="sale", db_column='SellerID', null=True)
    payment_type =  models.CharField(db_column='Payment_type', max_length=255, blank=True, null=True)
    status = models.SmallIntegerField(
        null=False,
        blank=False,
        default=ShippingStatus.DANG_XU_LY.value,
        choices=[
            (ShippingStatus.DANG_XU_LY.value, ShippingStatus.DANG_XU_LY.name),
            (ShippingStatus.DA_TIEP_NHAN.value, ShippingStatus.DA_TIEP_NHAN.name),
            (ShippingStatus.DANG_LAY_HANG.value, ShippingStatus.DANG_LAY_HANG.name),
            (ShippingStatus.DANG_GIAO_HANG.value, ShippingStatus.DANG_GIAO_HANG.name),
            (ShippingStatus.DA_GIAO.value, ShippingStatus.DA_GIAO.name),
            (ShippingStatus.HUY.value, ShippingStatus.HUY.name)
        ]
    )
    amount = models.FloatField(db_column='Amount', blank=True, default=0)  
    create_at = models.DateTimeField(db_column="create_at", auto_now=True)
    recv_name =  models.CharField(db_column='rcv_name', max_length=255, blank=True, null=True)
    recv_city = models.ForeignKey('City', models.CASCADE, db_column='city', null=True)
    recv_district =  models.ForeignKey('District', models.CASCADE, db_column='district', null=True)
    recv_street =  models.ForeignKey('Street', models.CASCADE, db_column='street', null=True)
    recv_house =  models.CharField(db_column='rcv_house', max_length=255, blank=True, null=True)
    recv_phone =  models.CharField(db_column='rcv_phone', max_length=255, blank=True, null=True)
    recv_email =  models.CharField(db_column='rcv_email', max_length=255, blank=True, null=True)
    note =  models.CharField(db_column='note', max_length=255, blank=True, null=True)
    ship =  models.FloatField(db_column='shipping_fee', blank=True, default=0)
    voucher =  models.ForeignKey('Voucher', models.CASCADE, db_column='voucher', null=True)

class OrderStatus(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    status = models.SmallIntegerField(
        null=False,
        blank=False,
        default=ShippingStatus.DANG_XU_LY.value,
        choices=[
            (ShippingStatus.DANG_XU_LY.value, ShippingStatus.DANG_XU_LY.name),
            (ShippingStatus.DA_TIEP_NHAN.value, ShippingStatus.DA_TIEP_NHAN.name),
            (ShippingStatus.DANG_LAY_HANG.value, ShippingStatus.DANG_LAY_HANG.name),
            (ShippingStatus.DANG_GIAO_HANG.value, ShippingStatus.DANG_GIAO_HANG.name),
            (ShippingStatus.DA_GIAO.value, ShippingStatus.DA_GIAO.name),
            (ShippingStatus.HUY.value, ShippingStatus.HUY.name)
        ]
    )
    order = models.ForeignKey('Order', models.CASCADE, db_column='OrderId')
    create_at = models.DateTimeField(db_column="create_at", auto_now=True)

class CustomerReview(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    rating = models.IntegerField(default=0)
    content = models.CharField(db_column='Content', max_length=255, blank=True, null=True)  # Field name made lowercase.
    customer = models.ForeignKey('User', models.CASCADE, db_column='UserID')
    product = models.ForeignKey('ProductVariant', models.CASCADE, db_column='VariantId')
    create_at = models.DateTimeField(db_column="create_at", auto_now=True)

class ShippingDepartment(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    desc = models.CharField(db_column='Desc', max_length=255, blank=True, null=True)  # Field name made lowercase.

class OrderShip(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    order = models.ForeignKey('Order', models.CASCADE, db_column='OrderId')
    ship = models.ForeignKey('ShippingDepartment', models.CASCADE, db_column='ShipId')
    price = models.FloatField(db_column='Price')  # Field name made lowercase.\
    estimated_arrival = models.DateTimeField(db_column="estimated_arrival", null=True)

class Favorite(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    customer = models.ForeignKey('User', models.CASCADE, db_column='UserID')
    product = models.ForeignKey('ProductVariant', models.CASCADE, db_column='VariantId')

class Reply(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    content = models.CharField(db_column='Content', max_length=255, blank=True, null=True)  # Field name made lowercase.
    staff = models.ForeignKey('User', models.CASCADE, db_column='UserID')
    review = models.ForeignKey('CustomerReview', models.CASCADE, db_column='CustomerReview')
class Brand(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=255, blank=True, null=True)  # Field name made lowercase.
    desc = models.CharField(db_column='Desc', max_length=255, blank=True, null=True)

class Author(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=255, blank=True, null=True)  # Field name made lowercase.
    desc = models.CharField(db_column='Desc', max_length=255, blank=True, null=True) 
    phone = models.CharField(db_column='Phone', max_length=255, blank=True, null=True)  # Field name made lowercase.

class Designer(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=255, blank=True, null=True)  # Field name made lowercase.
    desc = models.CharField(db_column='Desc', max_length=255, blank=True, null=True) 
    phone = models.CharField(db_column='Phone', max_length=255, blank=True, null=True)

class Publisher(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=255, blank=True, null=True)  # Field name made lowercase.
    desc = models.CharField(db_column='Desc', max_length=255, blank=True, null=True) 
    phone = models.CharField(db_column='Phone', max_length=255, blank=True, null=True)

class City(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    desc = models.CharField(db_column='Desc', max_length=255, blank=True, null=True)
class District(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    desc = models.CharField(db_column='Desc', max_length=255, blank=True, null=True)
    city = models.ForeignKey('City', models.CASCADE, db_column='city', null=True)
class Street(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    desc = models.CharField(db_column='Desc', max_length=255, blank=True, null=True)
    district = models.ForeignKey('District', models.CASCADE, db_column='district', null=True)

class ShippingAdress(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    house_number = models.CharField(db_column='HouseNumber', max_length=255, blank=True, null=True)  # Field name made lowercase.
    city = models.ForeignKey('City', models.CASCADE, db_column='city', null=True)
    district = models.ForeignKey('District', models.CASCADE, db_column='district', null=True)
    street = models.ForeignKey('Street', models.CASCADE, db_column='street', null=True)
    customer = models.ForeignKey('User', models.CASCADE, db_column='user', null=True)

class Voucher(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', max_length=255, blank=True, null=True)  # Field name made lowercase.
    desc = models.CharField(db_column='Desc', max_length=255, blank=True, null=True)
    sale =  models.FloatField(db_column='sale', max_length=255, blank=True, null=True)
    offset = models.FloatField(db_column='offset', max_length=255, blank=True, null=True)
    role = models.SmallIntegerField(
        null=False,
        blank=False,
        default=VoucherType.SHIPPING.value,
        choices=[
            (VoucherType.SHIPPING.value, VoucherType.SHIPPING.name),
            (VoucherType.ORDER.value, VoucherType.ORDER.name),
        ]
    )