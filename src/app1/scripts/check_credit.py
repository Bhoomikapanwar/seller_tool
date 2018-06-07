from app1.models import SellerBusinessDetails as Sbd , SellerDetails as Sd
from datetime import datetime,timedelta
from . import send_email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def check():
    f= open('/home/bhoomika/job1.txt','a')
    #expiry_period = datetime.now().date()+timedelta(days=20)
    #obj= Sbd.objects.filter(expiry_date = expiry_period)
    obj = Sbd.objects.all()
    for x in obj:
        delta = x.expiry_date - datetime.now().date()
        if delta < timedelta(days=20):
            obj1 = Sd.objects.get(sid=x.sid)
            text = 'Hello '+str(obj1.sname) + ', \nThis is to inform you that your credit card will expire in '+ str(delta.days) +' days.\nKindly update your credit card information to enjoy our uninterrupted services.\nRegards\nAmazon team.\n'
            sub = 'Amazon account update required'
            from1="schedulecronjob@gmail.com"
            #from1= 'schedulecronjob@gmail.com'
            to1=obj1.semail
            msg = send_email.create_msg(text,sub,from1,to1)
            send_email.sendemail(msg)
            f.writelines(str(delta))
            f.writelines(str(obj1.semail))
            del msg

def run(*args):
    check()
