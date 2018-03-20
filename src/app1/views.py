from django.shortcuts import render
from django.http import HttpResponse
from .forms import CreditCardForm
from .models import SellerBusinessDetails,SellerDetails
# Create your views here.

def home(request):
    response_html="<h1>Bhoomika</h1>"
    return HttpResponse(response_html)

def tryCredit(request):
    if request.method == 'POST':
        form = CreditCardForm(request.POST)
        #print("cjdbsk")
        """
        try:
            obj = SellerBusinessDetails.object.get(sid)
        """
        if form.is_valid():
            print(form.cleaned_data['credit_card_no'])
            s01 = SellerDetails.objects.get(sid="s001")
            obj = SellerBusinessDetails(sid=s01,credit_card_no=form.cleaned_data['credit_card_no'],expiry_date=form.cleaned_data['expiry_date'])
            obj.save()
            print(obj)
    else:
        form = CreditCardForm()
    return render(request,'credit_card_input.html',{'form':form})
