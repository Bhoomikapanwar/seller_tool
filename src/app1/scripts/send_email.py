import datetime
import sys
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def create_msg(text,sub,from1,to):
    msg = MIMEMultipart()       # create a message
    # setup the parameters of the message
    msg['From']=from1
    msg['To']= to
    msg['Subject']=sub
    # add in the message body
    msg.attach(MIMEText(text, 'plain'))
    return msg

def sendemail(msg):
    server = smtplib.SMTP(host='smtp.gmail.com',port= 587)
    server.starttls()
    server.login("bhoomika.mcs17.du@gmail.com", "etidestiny")
    #Email id to be used to send the emails
    #server.login("schedulecronjob@gmail.com", "kinam123")
    #Send the mail
    # send the message via the server set up earlier.
    server.send_message(msg)
    #server.sendmail("bhoomika.mcs17.du@gmail.com",emailid, msg)
