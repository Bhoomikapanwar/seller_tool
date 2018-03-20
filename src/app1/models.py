from django.db import models

# Create your models here.
class T(models.Model):
    no = models.IntegerField(primary_key='true')
    name = models.CharField(max_length=30,null=True)

class SellerDetails(models.Model):
    sid = models.CharField(primary_key=True,max_length=10)  # This field type is a guess.
    sname = models.CharField(max_length=30)

class SellerBusinessDetails(models.Model):
    sid = models.ForeignKey(SellerDetails,on_delete=models.CASCADE,related_name='+')
    credit_card_no = models.TextField(max_length=16)
    expiry_date = models.DateField(null=False)
