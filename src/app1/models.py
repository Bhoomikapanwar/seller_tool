from django.db import models
from django.core.validators import RegexValidator, MinLengthValidator, MaxLengthValidator
from django.contrib.auth.models import User

#ACCOUNT_STATUS
ACCOUNT_STATUS = (
    ('active','active'),
    ('blocked','blocked')
)

#FLAG CHOICES
FLAG_CHOICES =  (
    ('empty','empty'),
    ('inprocess','inprocess'),
    ('accepted','accepted'),
    ('rejected','rejected')
)

class SellerDetails(models.Model):
    sid = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    sname = models.CharField(max_length=30,null=False)
    semail = models.EmailField(max_length=254,null=False)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    sphone = models.CharField(validators=[phone_regex], max_length=17, null=False)
    scompany_name = models.TextField(null=False)
    sKYC = models.CharField(max_length=12,null=True,blank=True, unique=True)
    sKYC_flag = models.CharField(max_length=15,null=False,choices = FLAG_CHOICES, default='empty')
    account_status = models.CharField(max_length=15,null=False,choices = ACCOUNT_STATUS, default ='active' )

class SellerBankDetails(models.Model):
    sid = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    sbank_name = models.CharField(max_length=50,null=False,default='Indian bank')
    sacc_no = models.CharField(max_length=34,null=False)
    sifsc_code = models.CharField(max_length=50,null=False,default=0000)

class SellerBusinessDetails(models.Model):
    sid = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    credit_card_no = models.TextField(max_length=16,null=False)
    expiry_date = models.DateField(null=False)
    #gst_regex = RegexValidator(regex=r'^([0][1-9]|[1-2][0-9]|[3][0-5])([a-zA-Z]{5}[0-9]{4}[a-zA-Z]{1}[1-9a-zA-Z]{1}[zZ]{1}[0-9a-zA-Z]{1})+$' , message = "Please enter a valid GST Number")
    gst_no =  models.CharField(max_length=15,blank=True, null=True)
    gst_flag = models.CharField(max_length=15,null=False,choices = FLAG_CHOICES, default='empty')

    class Meta:
        indexes = [
            models.Index(fields=['expiry_date'], name='expiry_date_idx'),
        ]

class BaseTraitDetails(models.Model):
    sid = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    overall_value = models.DecimalField(max_digits=5,decimal_places=2,default=0)
    overall_value_health = models.DecimalField(max_digits=5,decimal_places=2,default=0)

    class Meta:
        abstract=True

class TraitValueDetails(BaseTraitDetails):
    late_shipment_rate = models.DecimalField(max_digits=5,decimal_places=2,default=0)
    on_time_delivery = models.DecimalField(max_digits=5,decimal_places=2,default=0)
    hit_to_success_ratio = models.DecimalField(max_digits=5,decimal_places=2,default=0)
    late_shipment_recommendations = models.TextField(default="ABC")
    positive_feedbacks = models.DecimalField(max_digits=5,decimal_places=2,default=0)
    negative_feedbacks = models.DecimalField(max_digits=5,decimal_places=2,default=0)

    gst_value =  models.DecimalField(max_digits=5,decimal_places=2,default=0)
    recommendations_gstValue = models.TextField(max_length = 100,null=True)

    kyc_value =  models.DecimalField(max_digits=5,decimal_places=2,default=0)
    recommendations_kycValue = models.TextField(max_length = 100,null=True)

    credit_card_value =  models.DecimalField(max_digits=5,decimal_places=2,default=0)
    recommendations_creditCardValue = models.TextField(max_length = 100,null=True)

    class Meta:
        managed=True
        db_table='traits_value_details'
