from . import send_email
from app1.models import SellerDetails as Sd
from django.contrib.auth.models import User

from .import gen_noti

def notify_gst(obj):
    print(obj)
    #print("Hey1")
    sid = obj['data']['sid_id']
    obj1 = Sd.objects.get(sid = sid)
    #print(obj1.sid)
    usr = User.objects.get(username = obj1.sid)
    print(usr)
    tomail = obj1.semail
    name = obj1.sname
    frommail = "bhoomika.mcs17.du@gmail.com"

    if(obj['data']['gst_flag'] == 'inprocess'):
        text= 'Hello '+ name + ', \nThis is to inform you that your GST information validation is in process. \nWe\'ll notify you of any updates in regarding to the same.\nRegards\nAmazon team.\n'
        sub = "Amazon account GST information"
        m = send_email.create_msg(text,sub,frommail,tomail)
        msg = "Your gst verification is in process"
        print("Hello1")
        gen_noti.gen_notify(usr,msg)
        print("Hello2")
        #print(m)
        #print(tomail)
        print("Hello3")
        #send_email.sendemail(m)
        print("hello4")
    elif(obj['data']['gst_flag'] == 'accepted'):
        text= 'Hello '+ name + ', \nCongratulations, this is to inform you that your GST information validation is successfully completed.\nRegards\nAmazon team.\n'
        sub = "Amazon account GST information"
        m = send_email.create_msg(text,sub,frommail,tomail)
        msg = "Your gst details has been accepted"
        #print(m)
        gen_noti.gen_notify(usr,msg)
        print(msg)
        print(tomail)
        #send_email.sendemail(m)
    elif(obj['data']['gst_flag'] == 'rejected'):
        text= 'Hello '+ name + ', \nThis is to inform you that your GST information validation has been rejected due to incorrect information. \nKindly correct the kyc details provided by you and submit again for validation.\nRegards\nAmazon team.\n'
        sub = "Amazon account GST information"
        m = send_email.create_msg(text,sub,frommail,tomail)
        msg = "Your gst details has been rejected"
        gen_noti.gen_notify(usr,msg)
        #print(m)
        print(msg)
        print(tomail)
        #send_email.sendemail(m)
    else:
        print("Hey2")
