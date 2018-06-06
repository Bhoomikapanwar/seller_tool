import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import eventlet
from eventlet.hubs import trampoline
import json
from app1.models import SellerBusinessDetails as Sbd , SellerDetails as Sd
from django.contrib.auth.models import User

from .import check_kyc
from .import check_gst

dsn = "dbname=proj1_1 user=bhoomika password=bhoomika"  # customise this

def dblisten(q):
    """
    Open a db connection and add notifications to *q*.
    """
    cnn = psycopg2.connect(dsn)
    cnn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cur = cnn.cursor()
    cur.execute("LISTEN data;")
    while 1:
        trampoline(cnn, read=True)
        cnn.poll()
        while cnn.notifies:
            n = cnn.notifies.pop()
            q.put(n)

def handle():
    """
    Receive a connection and send it database notifications.
    """
    q = eventlet.Queue()
    eventlet.spawn(dblisten,q)
    while 1:
        n = q.get()
        #print(n.payload)
        #print(isinstance(n.payload,str))
        #m=json.dumps(n.payload)
        #print(isinstance(o,str))
        o=json.loads(n.payload)
        #print(o['data']['sid_id'])
        if('gst_flag' in o['data']):
            print(o)
            check_gst.notify_gst(o)

        elif('sKYC_flag' in o['data']):
            print(o)
            check_kyc.notify_kyc(o)
        """
        USING psycopg2 FOR QUERY EXECUTIONS
        #cnn1 = psycopg2.connect(dsn)
        #cnn1.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        #cur1 = cnn1.cursor()
        #cur1.execute("select name from app1_t where no={0};".format(o['data']['no']))
        #for record in cur1:
        #    print(record)
        """
        #ws.send(n.payload)

def run(*args):
    handle()
