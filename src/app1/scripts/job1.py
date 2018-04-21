import datetime
import sys
import smtplib


def sendemail(msg):
    server = smtplib.SMTP(host='smtp.gmail.com',port= 587)
    server.starttls()
    server.login("schedulecronjob@gmail.com", "bhoomika")
    #Send the mail
    # send the message via the server set up earlier.
    server.send_message(msg)
    #server.sendmail("bhoomika.mcs17.du@gmail.com",emailid, msg)
