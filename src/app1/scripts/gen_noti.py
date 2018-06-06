from notifications.signals import notify
from notifications.models import Notification
from django.contrib.auth.models import User

def gen_notify(usr,msg):
    print(usr)
    print(msg)
    notify.send(usr,recipient=usr,verb=msg)
