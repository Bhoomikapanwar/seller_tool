# Generated by Django 2.0.3 on 2018-04-01 22:21

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sellerbankdetails',
            old_name='s_accno',
            new_name='sacc_no',
        ),
        migrations.AddField(
            model_name='sellerbankdetails',
            name='sbank_name',
            field=models.CharField(default='Indian bank', max_length=50),
        ),
        migrations.AddField(
            model_name='sellerbankdetails',
            name='sifsc_code',
            field=models.CharField(default=0, max_length=50),
        ),
        migrations.AddField(
            model_name='sellerbusinessdetails',
            name='gst_flag',
            field=models.CharField(choices=[('inprocess', 'inprocess'), ('validated', 'validated'), ('not validated', 'not validated')], default='not validated', max_length=15),
        ),
        migrations.AddField(
            model_name='sellerbusinessdetails',
            name='gst_no',
            field=models.CharField(default='0123456789677Z9', max_length=15, validators=[django.core.validators.RegexValidator(message='Please enter a valid GST Number', regex='^([0][1-9]|[1-2][0-9]|[3][0-5])([a-zA-Z]{5}[0-9]{4}[a-zA-Z]{1}[1-9a-zA-Z]{1}[zZ]{1}[0-9a-zA-Z]{1})+$')]),
        ),
        migrations.AlterField(
            model_name='sellerdetails',
            name='scompany_name',
            field=models.TextField(),
        ),
    ]
