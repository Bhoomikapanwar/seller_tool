# Generated by Django 2.0.3 on 2018-06-05 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0010_auto_20180605_0903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='traitvaluedetails',
            name='credit_card_value',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='traitvaluedetails',
            name='gst_value',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='traitvaluedetails',
            name='kyc_value',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
    ]
