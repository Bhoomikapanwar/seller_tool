# Generated by Django 2.0.3 on 2018-06-05 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0008_auto_20180425_1543'),
    ]

    operations = [
        migrations.AddField(
            model_name='traitvaluedetails',
            name='recommendations_creditCardValue',
            field=models.TextField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='traitvaluedetails',
            name='recommendations_gstValue',
            field=models.TextField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='traitvaluedetails',
            name='recommendations_kycValue',
            field=models.TextField(max_length=100, null=True),
        ),
    ]
