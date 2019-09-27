#!/usr/bin/python
from datetime import datetime
from elasticsearch import Elasticsearch
es = Elasticsearch(["http://172.31.0.72:9200"])

res = es.search(index="logstash-*", body={"query": {"match_all": {}}})
print("Got %d Hits:" % res['hits']['total'])

for hit in res['hits']['hits']:
    print(hit["_source"])
