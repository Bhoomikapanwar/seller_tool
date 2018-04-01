import datetime
import sys
import smtplib

#with open('dateInfo.txt','a') as outFile:
#    outFile.write('\n'+str(datetime.datetime.now()))
f = open('/home/bhoomika/write_date.txt','a')
f.writelines(str(datetime.datetime.now()))
for x in sys.argv:
    f.writelines(x)

server = smtplib.SMTP(host='smtp.gmail.com',port= 587)
server.starttls()
#Next, log in to the server
server.login("bhoomika.mcs17.du@gmail.com", "enter password here")
#server.ehlo()

#server.ehlo()

#Send the mail
msg = "\nHello Bhoomika" # The /n separates the message from the headers
server.sendmail("bhoomika.mcs17.du@gmail.com",str(sys.argv[1]), msg)

f.close()
