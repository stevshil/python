#!/usr/bin/env python
#import gspread
#from oauth2client.service_account import ServiceAccountCredentials
#import pprint
#from googleapiclient import discovery
#import csv
import json
import pygsheets

fh=open("chart2.json","r")
chart=fh.read()
fh.close()
obj=json.loads(chart)
sheetID='1ilBIlml-upQDmV1IRRjxC-74_GxWjuGHnXlqJRqU8bY'

ct=pygsheets.custom_types.ChartType("BAR")

gc=pygsheets.authorize(service_file='mysecret.json')
ss=gc.open('TestSheet')
print(ss.worksheets())
wks=ss.worksheet('index',0)
chart=pygsheets.Chart(wks,domain=('A1','A5'),ranges=[('C1','C5'),('D1','D5')],chart_type=ct,title="Jasmins Chart",anchor_cell="F3")
