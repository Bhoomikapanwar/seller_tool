from crontab import CronTab
from datetime import datetime
from app1.models import SellerBusinessDetails as Sbd , SellerDetails as Sd
def tut(sid1):
    obj = Sbd.objects.get(sid=sid1)
    obj1 = Sd.objects.get(sid=sid1)
    my_cron = CronTab(user='bhoomika')
    print(obj.sid,obj1)
    job = my_cron.new(command='python /home/bhoomika/django-dev/proj1/src/app1/scripts/job1.py {0}'.format(obj1.semail),comment=sid1)
    job.minute.every(1)
    #job.setall(datetime(2019,3,23,13,49))
    my_cron.write()
"""
    for job in my_cron:
        my_cron.remove(job)
        my_cron.write()
"""
