from django.db import models
from django.core.validators import RegexValidator, MinLengthValidator, MaxLengthValidator
from django.contrib.auth.models import User

class SellerDetails(models.Model):
    sid = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    sname = models.CharField(max_length=30,null=False)
    semail = models.EmailField(max_length=254,null=False)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    sphone = models.CharField(validators=[phone_regex], max_length=17, null=False)
    scompany_name = models.CharField(max_length=100,null=False)

class SellerBankDetails(models.Model):
    sid = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    s_accno = models.CharField(max_length=34,null=False)

class SellerBusinessDetails(models.Model):
    sid = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    credit_card_no = models.TextField(max_length=16,null=False)
    expiry_date = models.DateField(null=False)
