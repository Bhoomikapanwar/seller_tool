import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import eventlet
from eventlet.hubs import trampoline
import json
from app1.models import T
dsn = "dbname=proj1 user=hp password=bhoomika"  # customise this

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
    eventlet.spawn(dblisten, q)
    while 1:
        n = q.get()
        print(n.payload)
        #print(isinstance(n.payload,str))
        #m=json.dumps(n.payload)
        #print(isinstance(o,str))
        o=json.loads(n.payload)
        #print(n.payload)
        #print(o['data']['no'],"Hello")
        obj = T.objects.get(no=o['data']['no'])
        print(obj.no,obj.name)
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
