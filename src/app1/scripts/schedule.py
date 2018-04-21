from crontab import CronTab
from datetime import datetime
def cron_sch():
    my_cron = CronTab(user='bhoomika')
    #Make appropriate changes in the paths in the below line
    job1 = my_cron.new(command =' . /home/bhoomika/.bashrc && . /home/bhoomika/gitRepos/bin/activate && python /home/bhoomika/gitRepos/seller_tool/src/manage.py runscript check_credit', comment="creditcard")
    #to schedule job everyday @ 9:00
    #job1.minute.on(0)
    #job1.hour.on(9)

    """ to check the schedule of jobs
    for job in my_cron:
        sch = job.schedule(date_from = datetime.now())      #crontier package
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
