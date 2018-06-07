# Generated by Django 2.0.3 on 2018-04-25 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_auto_20180419_0625'),
    ]

    operations = [
        migrations.AddField(
            model_name='sellerdetails',
            name='account_status',
            field=models.CharField(choices=[('active', 'active'), ('blocked', 'blocked')], default='active', max_length=15),
        ),
        migrations.AddIndex(
            model_name='sellerbusinessdetails',
            index=models.Index(fields=['expiry_date'], name='expiry_date_idx'),
        ),
    ]