from crontab import CronTab
from datetime import datetime
def cron_sch():
    my_cron = CronTab(user='bhoomika')
    #Make appropriate changes in the paths in the below line
    #create a new cron job
    job1 = my_cron.new(command =' . /home/bhoomika/.bashrc && . /home/bhoomika/django-dev/proj1/bin/activate && python /home/bhoomika/django-dev/proj1/src/manage.py runscript check_credit', comment="creditcard")
    #to schedule job everyday @ 9:00
    #job1.minute.on(0)
    #job1.hour.on(9)

    """ to check the schedule of jobs
    for job in my_cron:
        sch = job.schedule(date_from = datetime.now())     #croniter package
        print(sch.get_next())
        print(sch.get_next())
        print(sch.get_next())
        print(sch.get_next())
        print(sch.get_next())
        print(sch.get_next())
        print(sch.get_next())
        print(sch.get_next())
    """

    job1.minute.every(1)
    my_cron.write()

    """
    for job in my_cron:
        my_cron.remove(job)
        my_cron.write()
    """

def run(*args):
    cron_sch()
