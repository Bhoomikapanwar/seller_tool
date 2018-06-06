from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import CreditCardForm
from .models import SellerBusinessDetails,SellerDetails,SellerBankDetails
from django.http import Http404
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from datetime import datetime,timedelta

from django.shortcuts import render
#from dashboard.models import *
from django.db.models import Count, F, Sum
from abc import ABC, abstractmethod
import re
from .calculate import *
# Create your views here.

def logredi(request):
    if request.user.groups.filter(name="Seller"):
        if SellerDetails.objects.filter(sid=request.user).exists():
            obj = SellerDetails.objects.get(sid=request.user)
            obj1 = SellerBusinessDetails.objects.get(sid=request.user)
            expiry_period = datetime.now().date()+timedelta(days=20)
            if obj1.expiry_date == expiry_period:
                obj.account_status = 'blocked'

            if obj.account_status == 'active':
                return redirect('/gst/')        #redirect to home instead
            elif obj.account_status == 'blocked':
                return render(request,'credit_card_input.html',{'account_status':obj.account_status})
        else:
            logout(request)
            raise Http404("invalid user")
    else:
            logout(request)
            raise Http404("invalid user")

@login_required(login_url="/login/")
def profile(request):
            obj = SellerDetails.objects.get(sid=request.user)
            obj1 = SellerBusinessDetails.objects.get(sid=request.user)
            obj2 = SellerBankDetails.objects.get(sid=request.user)
            return render(request,'profile.html',{'obj':obj, 'obj1':obj1 ,'obj2':obj2})

@login_required(login_url="/login/")
def noti(request):
    usr = User.objects.get(username=request.user)
    #print(obj)
    noti  = usr.notifications.all()
    return render(request,'health.html',{})

@login_required(login_url="/login/")
def Credit(request):
    if request.method == 'POST':
        form = CreditCardForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['credit_card_no'])
            s01 = SellerDetails.objects.get(sid=request.user)
            obj = SellerBusinessDetails(sid=request.user,credit_card_no=form.cleaned_data['credit_card_no'],expiry_date=form.cleaned_data['expiry_date'])
            obj.save()
    else:
        form = CreditCardForm()
    return render(request,'credit_card_input.html',{'form':form})


@login_required(login_url="/login/")
def gst(request):
    if SellerDetails.objects.filter(sid=request.user).exists():
        if request.method == "POST":
            gst_no = request.POST['gst_no']
            obj = SellerBusinessDetails.objects.get(sid=request.user)
            obj.gst_no = gst_no
            obj.gst_flag = 'inprocess'
            obj.save()
            return render(request,"gst.html",{'gst_flag':obj.gst_flag})
        else:
            obj = SellerBusinessDetails.objects.get(sid=request.user)
            return render(request,"gst.html",{'gst_flag':obj.gst_flag})
    else:
        logout(request)
        raise Http404("invalid user")

@login_required(login_url="/login/")
def kyc(request):
    if SellerDetails.objects.filter(sid=request.user).exists():
        if request.method == "POST":
            kyc_no = request.POST['kyc_no']
            obj = SellerDetails.objects.get(sid=request.user)
            obj.sKYC = kyc_no
            obj.sKYC_flag = 'inprocess'
            obj.save()
            return render(request,"kyc.html",{'kyc_flag':obj.sKYC_flag})
        else:
            obj = SellerDetails.objects.get(sid=request.user)
            return render(request,"kyc.html",{'kyc_flag':obj.sKYC_flag})
    else:
        logout(request)
        raise Http404("invalid user")

@login_required(login_url="/login/")
def main(request):
    sid=request.user
    trait_name = []
    trait_value = []
    recommendation_list = []
    for cls in Trait.__subclasses__():

        class_name = cls.__name__
        trait_component = re.sub( '(?<!^)(?=[A-Z])', '_', class_name ).lower()
        obj = cls(trait_component)
        obj.template_method(trait_name, trait_value, recommendation_list,request)

    recommendation_trait_list = zip(trait_name, trait_value, recommendation_list)
    print(trait_name)
    print(trait_value)
    print(recommendation_list)
    print(recommendation_trait_list)
    return render(request,'health.html',{'recommendation_trait_list':recommendation_trait_list})
