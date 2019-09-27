#!/usr/bin/python
from datetime import datetime
from elasticsearch import Elasticsearch
es = Elasticsearch(["http://172.31.0.72:9200"])

# https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl-exists-query.html

doc = {
  "query": {
    "bool": {
      "must": [
        {"match": { "type": "applog" } }, 
        {"exists": { "field": "stockName"}},
      ],
    }
  },
  "sort": ["_doc"],
  "size": 10000
}

res = es.search(index="",body=doc,scroll='1m')
print("Got %d Hits:" % res['hits']['total'])
sid = res['_scroll_id']
scroll_size = res['hits']['total']

while (scroll_size > 0):
  for hit in res['hits']['hits']:
    print(hit["_source"])
  page = es.scroll(scroll_id = sid, scroll = '2m')
  sid = page['_scroll_id']
  scroll_size = len(page['hits']['hits'])
