from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import CreditCardForm
from .models import SellerBusinessDetails,SellerDetails,SellerBankDetails
from django.http import Http404
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.

@login_required(login_url="/login/")
def home(request):
    response_html="<h1>Bhoomika</h1>"
    return HttpResponse(response_html)

@login_required(login_url="/login/")
def noti(request):
    usr = User.objects.get(username=request.user)
    noti  = usr.notifications.all()
    print(noti)
    return render(request,'notifications.html',{'notices':noti})

def Credit(request):
    if request.method == 'POST':
        form = CreditCardForm(request.POST)
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

def logredi(request):
    if request.user.groups.filter(name="Seller"):
        if SellerDetails.objects.filter(sid=request.user).exists():
            return redirect('/gst/')
        else:
            logout(request)
            raise Http404("invalid user")
    else:
            logout(request)
            raise Http404("invalid user")


@login_required(login_url="/login/")
def gst(request):
    if SellerDetails.objects.filter(sid=request.user).exists():
        obj = SellerDetails.objects.get(sid=request.user)
        return render(request,"gst.html",{'obj':obj})
    else:
        logout(request)
        raise Http404("invalid user")

@login_required(login_url="/login/")
def kyc(request):
    if SellerDetails.objects.filter(sid=request.user).exists():
        obj = SellerDetails.objects.get(sid=request.user)
        return render(request,"kyc.html",{'obj':obj})
    else:
        logout(request)
        raise Http404("invalid user")
