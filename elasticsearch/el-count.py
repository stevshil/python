#!/usr/bin/python
from datetime import datetime
from elasticsearch import Elasticsearch
es = Elasticsearch(["http://172.31.0.72:9200"])

doc={
  "query": {
    "match": {
      "type": "applog"
    }
  }
}

res = es.search(index="logstash-*", body=doc)
print("Got %d Hits:" % res['hits']['total'])
