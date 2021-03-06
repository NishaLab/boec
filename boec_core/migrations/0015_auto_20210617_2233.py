# Generated by Django 3.1.7 on 2021-06-17 15:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('boec_core', '0014_user_userlink'),
    ]

    operations = [
        migrations.CreateModel(
            name='Voucher',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('code', models.CharField(blank=True, db_column='Code', max_length=255, null=True)),
                ('desc', models.CharField(blank=True, db_column='Desc', max_length=255, null=True)),
                ('sale', models.FloatField(blank=True, db_column='sale', max_length=255, null=True)),
                ('role', models.SmallIntegerField(choices=[(1, 'SHIPPING'), (2, 'ORDER')], default=1)),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='ship',
            field=models.FloatField(blank=True, db_column='shipping_fee', default=0),
        ),
        migrations.AddField(
            model_name='order',
            name='voucher',
            field=models.ForeignKey(db_column='voucher', null=True, on_delete=django.db.models.deletion.CASCADE, to='boec_core.voucher'),
        ),
    ]
