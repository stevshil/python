#!/usr/bin/python
from datetime import datetime
from elasticsearch import Elasticsearch
es = Elasticsearch(["http://172.31.0.72:9200"])

#res = es.search(index="logstash-*", body={"query": {"match_all": {}}})
#print("Got %d Hits:" % res['hits']['total'])

doc = {
	'size': 10000,
	'query': {
		'match_all': {}
	}
}

res = es.search(index="logstash-*",doc_type='myType', body=doc,scroll='1m')
scroll = res['_scroll_id']
res2 = es.scroll(scroll_id = scroll, scroll = '1m')

for hit in res['hits']['hits']:
    print(hit["_source"])
