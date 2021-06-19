# Generated by Django 3.1.7 on 2021-06-16 14:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('boec_core', '0011_auto_20210605_0832'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, db_column='Name', max_length=255, null=True)),
                ('desc', models.CharField(blank=True, db_column='Desc', max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, db_column='Name', max_length=255, null=True)),
                ('desc', models.CharField(blank=True, db_column='Desc', max_length=255, null=True)),
                ('city', models.ForeignKey(db_column='city', null=True, on_delete=django.db.models.deletion.CASCADE, to='boec_core.city')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='recv_house',
            field=models.CharField(blank=True, db_column='rcv_house', max_length=255, null=True),
        ),
        migrations.CreateModel(
            name='VariantOption',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('quantity', models.IntegerField(default=0)),
                ('price', models.FloatField(db_column='Price')),
                ('name', models.CharField(blank=True, db_column='name', max_length=255, null=True)),
                ('product', models.ForeignKey(db_column='VariantId', on_delete=django.db.models.deletion.CASCADE, to='boec_core.productvariant')),
            ],
        ),
        migrations.CreateModel(
            name='Street',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, db_column='Name', max_length=255, null=True)),
                ('desc', models.CharField(blank=True, db_column='Desc', max_length=255, null=True)),
                ('district', models.ForeignKey(db_column='district', null=True, on_delete=django.db.models.deletion.CASCADE, to='boec_core.district')),
            ],
        ),
        migrations.CreateModel(
            name='ShippingAdress',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('house_number', models.CharField(blank=True, db_column='HouseNumber', max_length=255, null=True)),
                ('city', models.ForeignKey(db_column='city', null=True, on_delete=django.db.models.deletion.CASCADE, to='boec_core.city')),
                ('customer', models.ForeignKey(db_column='user', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('district', models.ForeignKey(db_column='district', null=True, on_delete=django.db.models.deletion.CASCADE, to='boec_core.district')),
                ('street', models.ForeignKey(db_column='street', null=True, on_delete=django.db.models.deletion.CASCADE, to='boec_core.street')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='recv_district',
            field=models.ForeignKey(db_column='district', null=True, on_delete=django.db.models.deletion.CASCADE, to='boec_core.district'),
        ),
        migrations.AddField(
            model_name='order',
            name='recv_street',
            field=models.ForeignKey(db_column='street', null=True, on_delete=django.db.models.deletion.CASCADE, to='boec_core.street'),
        ),
        migrations.AlterField(
            model_name='order',
            name='recv_city',
            field=models.ForeignKey(db_column='city', null=True, on_delete=django.db.models.deletion.CASCADE, to='boec_core.city'),
        ),
        migrations.AlterField(
            model_name='orderedproduct',
            name='product',
            field=models.ForeignKey(db_column='OptionId', on_delete=django.db.models.deletion.CASCADE, to='boec_core.variantoption'),
        ),
    ]