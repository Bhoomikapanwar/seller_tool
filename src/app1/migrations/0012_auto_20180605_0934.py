# Generated by Django 2.0.3 on 2018-06-05 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0011_auto_20180605_0929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='traitvaluedetails',
            name='hit_to_success_ratio',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='traitvaluedetails',
            name='late_shipment_rate',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='traitvaluedetails',
            name='negative_feedbacks',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='traitvaluedetails',
            name='on_time_delivery',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='traitvaluedetails',
            name='overall_value',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='traitvaluedetails',
            name='overall_value_health',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='traitvaluedetails',
            name='positive_feedbacks',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
    ]
