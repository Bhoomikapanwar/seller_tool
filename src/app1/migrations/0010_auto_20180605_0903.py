# Generated by Django 2.0.3 on 2018-06-05 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0009_auto_20180605_0902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sellerbusinessdetails',
            name='gst_no',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
