from notifications.signals import notify
from notifications.models import Notification
from django.contrib.auth.models import User
def test1():
    usr = User.objects.all()
    for u in usr:
        notify.send(u,recipient=u,verb="reached level 300")
    n = Notification.objects.unread()
    #u1 = User.objects.get(username="gilu")
    #n.mark_all_as_read(recipient=u1)
    #print(u1.notifications.unread())
    print(n)
    print("sent: ",n.sent())
    print("read: ",n.read())


    #for o in n:
    #    print(o)
def run(*args):
    test1()
