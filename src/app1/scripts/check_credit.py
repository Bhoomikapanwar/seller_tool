from app1.models import SellerBusinessDetails as Sbd , SellerDetails as Sd
from datetime import datetime,timedelta
from . import job1
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def check():
    f= open('/home/bhoomika/job1.txt','a')
    obj = Sbd.objects.all()
    for x in obj:
        delta = x.expiry_date - datetime.now().date()
        if delta < timedelta(days=20):
            obj1 = Sd.objects.get(sid=x.sid)
            msg = MIMEMultipart()       # create a message
            text = 'Hello '+str(obj1.sname) + ', \nThis is to inform you that your credit card will expire in '+ str(delta.days) +' days.\nKindly update your credit card information to enjoy our uninterrupted services.\nRegards\nAmazon team.\n'
            sub = 'Amazon account update required'
            # setup the parameters of the message
            msg['From']="bhoomika.mcs17.du@gmail.com"
            msg['To']=obj1.semail
            msg['Subject']=sub

            # add in the message body
            msg.attach(MIMEText(text, 'plain'))
            job1.sendemail(msg)
            f.writelines(str(delta))
            f.writelines(str(obj1.semail))

            del msg
            check()

def run(*args):
