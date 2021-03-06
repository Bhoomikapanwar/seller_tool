from elasticsearch_dsl.connections import connections
from elasticsearch_dsl import DocType,Integer, Text, Date,Search
from elasticsearch.helpers import bulk
from elasticsearch import Elasticsearch,helpers
from . import models
from datetime import datetime
from dashboard.models import Products
from es_synonyms import load_synonyms
from elasticsearch_dsl import analyzer,token_filter
connections.create_connection()


class Feedbacks_Index(DocType):
   
    id = Text()
    pid_seller = Text()
    feedbackdate = Date()
    rating_points = Integer()
    feedback_entered = Text()
                    
    '''feedback_entered = Text(analyzer=analyzer('wordnet_synonym_analyzer',
                                        tokenizer="standard",
                                        filter=["lowercase",
                                                token_filter('synonym',
                                                            type='synonym',
                                                            synonyms_path="analysis/synonym.txt"
                                                            )
                                                ]
                                    )
                    )'''

    class Meta:
        index = 'feedback-index'

def bulk_indexing(current_sellerid):
    Feedbacks_Index.init()
    es = Elasticsearch()
    productidlist = []
    sellerPid = Products.objects.all().filter(sid=current_sellerid).values('id')
    for sellerpid in sellerPid:
        for key,productid in sellerpid.items():
            productidlist.append(productid)
    bulk(client=es, actions=(b.indexing() for b in models.Feedbacks.objects.filter(product_id__in = productidlist).iterator()))
    

'''def search_keyword(keyword):
    synonym_tokenfilter = token_filter('my_tokenfilter', type = 'synonym',synonyms_path="analysis/wn_s.pl")
    synonym_analyzer = analyzer('wordnet_synonym_analyzer', tokenfilter='standard',filter=['lowercase',synonym_tokenfilter])
    s=Search().filter({
                        "match" : {
                                    "feedback_entered" : {
                                            "query" : keyword,
                                            "analyzer" : "wordnet_synonym_analyzer"
                                                }
                                        }
                    })
    response=s.execute()
    #for h in s.scan():
        #print(h.id ,": " ,h.feedback)
    return response
    print('Total %d hits found.' % response.hits.total)'''

'''def search_pid(pid_seller):
    p = h.filter('match',pid_seller=pid_seller)
    response = p.execute()
    response_dict = {}
    for h in p.scan():
        response_dict[h.id] = h.feedback_entered
    return response_dict

def search_rating(rating_points):
    s = Search().filter('term',rating_points=rating_points)
    response = s.execute()
    response_dict = {}
    for h in s.scan():
        response_dict[h.id] = h.feedback_entered
    return response_dict

def search_date(startdate,enddate):
    s = Search().filter('range',feedbackdate = {'gte': startdate , 'lte': enddate})
    response = s.execute()
    response_dict = {}
    for h in s.scan():
        response_dict[h.id] = [h.feedbackdate, h.feedback_entered]
    return response_dict'''

'''def search_many(startdate,enddate,rating_points,pid_seller):
    p = Search().filter('range',feedbackdate = {'gte': startdate , 'lte': enddate}).filter('term',rating_points=rating_points).filter('match',pid_seller=pid_seller)
    response = p.execute()
    response_dict = {}
    for h in p.scan():
        response_dict[h.id] = h.feedback_entered
    return response_dict'''

'''def f():
    s = Search()
    PolarityObj = polarity()
    feedbacks_id = []
    count = 0
    for doc in s.scan():
        IsNegative = PolarityObj.negative_feedbacks(doc.feedback)
        if IsNegative == True:
            feedbacks_id.append(doc.feedback_date)
            print(doc.feedback_date,'    ')
            count+=1
    print(count,'\n')
    #print(feedbacks_id)
    filteredDocuments = s.filter('terms',feedback_date=feedbacks_id)
    #filteredDocuments = s.query({"match_phrase": {"feedback":feedbacks_id} })
    r = filteredDocuments.execute()
    d={}
    m=0
    for h in filteredDocuments.scan():
        d[h.id] = h.feedback
        print(h.feedback_date,'  ')
        m+=1
    print(m)
    return d'''