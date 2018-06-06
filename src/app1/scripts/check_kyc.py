from . import send_email
def notify_kyc(obj):
    tomail= str(obj['data']['semail'])
    frommail = "bhoomika.mcs17.du@gmail.com"
    name = str(obj['data']['sname'])
    if(obj['data']['sKYC_flag'] == 'inprocess'):
        text= 'Hello '+name + ', \nThis is to inform you that your KYC information validation is in process. \nWe\'ll notify you of any updates in regarding to the same.\nRegards\nAmazon team.\n'
        sub = "Amazon account KYC information"
        m = send_email.create_msg(text,sub,frommail,tomail)
        #print(m)
        print(tomail)
        send_email.sendemail(m)
    elif(obj['data']['sKYC_flag'] == 'accepted'):
        text= 'Hello '+name + ', \nCongratulations, this is to inform you that your KYC information validation is successfully completed.\nRegards\nAmazon team.\n'
        sub = "Amazon account KYC information"
        m = send_email.create_msg(text,sub,frommail,tomail)
        #print(m)
        print(tomail)
        send_email.sendemail(m)
    elif(obj['data']['sKYC_flag'] == 'rejected'):
        text= 'Hello '+ name + ', \nThis is to inform you that your KYC information validation has been rejected due to incorrect information. \nKindly correct the kyc details provided by you and submit again for validation.\nRegards\nAmazon team.\n'
        sub = "Amazon account KYC information"
        m = send_email.create_msg(text,sub,frommail,tomail)
        #print(m)
        print(tomail)
        send_email.sendemail(m)
