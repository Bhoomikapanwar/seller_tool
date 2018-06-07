from . import send_email
from .import gen_noti
from app1.models import SellerDetails as Sd
from django.contrib.auth.models import User
def notify_kyc(obj):
    tomail= str(obj['data']['semail'])
    frommail = "schedulecronjob@gmail.com"
    sid = obj['data']['sid_id']
    name = str(obj['data']['sname'])
    obj1 = Sd.objects.get(sid = sid)
    usr = User.objects.get(username = obj1.sid)
    if(obj['data']['sKYC_flag'] == 'inprocess'):
        text= 'Hello '+name + ', \nThis is to inform you that your KYC information validation is in process. \nWe\'ll notify you of any updates in regarding to the same.\nRegards\nAmazon team.\n'
        sub = "Amazon account KYC information"
        m = send_email.create_msg(text,sub,frommail,tomail)
        #print(m)
        msg = "Your KYC verification is in process"
        #print("Hello1")
        gen_noti.gen_notify(usr,msg)
        print(tomail)
        send_email.sendemail(m)
    elif(obj['data']['sKYC_flag'] == 'accepted'):
        text= 'Hello '+name + ', \nCongratulations, this is to inform you that your KYC information validation is successfully completed.\nRegards\nAmazon team.\n'
        sub = "Amazon account KYC information"
        m = send_email.create_msg(text,sub,frommail,tomail)
        msg = "Your KYC details has been accepted"
        #print(m)
        gen_noti.gen_notify(usr,msg)
        #print(m)
        print(tomail)
        send_email.sendemail(m)
    elif(obj['data']['sKYC_flag'] == 'rejected'):
        text= 'Hello '+ name + ', \nThis is to inform you that your KYC information validation has been rejected due to incorrect information. \nKindly correct the kyc details provided by you and submit again for validation.\nRegards\nAmazon team.\n'
        sub = "Amazon account KYC information"
        m = send_email.create_msg(text,sub,frommail,tomail)
        msg = "Your gst details has been rejected"
        gen_noti.gen_notify(usr,msg)
        #print(m)
        print(tomail)
        send_email.sendemail(m)
