#!/usr/bin/python
from datetime import datetime
from elasticsearch import Elasticsearch
es = Elasticsearch(["http://172.31.0.72:9200"])

doc = {
  "query": {
    "match_all": {}
  },
  "sort": ["_doc"],
  "size": 10000
}

res = es.search(index="",body=doc,scroll='1m')
print("Got %d Hits:" % res['hits']['total'])

for hit in res['hits']['hits']:
    print(hit["_source"])
