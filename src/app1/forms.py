from django import forms
from .models import SellerBusinessDetails
from .fields import CreditCardField, ExpiryDateField
class CreditCardForm(forms.Form):
    credit_card_no = CreditCardField()
    expiry_date = ExpiryDateField()
