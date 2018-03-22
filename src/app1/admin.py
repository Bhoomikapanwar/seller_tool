from django.contrib import admin
from .models import SellerDetails,SellerBusinessDetails,SellerBankDetails
# Register your models here.
admin.site.register(SellerDetails)
admin.site.register(SellerBankDetails)
admin.site.register(SellerBusinessDetails)
