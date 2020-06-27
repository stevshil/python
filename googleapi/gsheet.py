#!/usr/bin/env python
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint
from googleapiclient import discovery
import csv
import json
import pygsheets

scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('mysecret.json', scope)
client = gspread.authorize(creds)
service = discovery.build('sheets', 'v4', credentials=creds)

sheet = client.open('FinalData').sheet1

#need to import this as a variable
dict_data = [{'name': 'chrus', 'yn': 20, 'skill': 80, 'affinity': 100, 'msg': []}, {'name': 'chras', 'yn': 16, 'skill': 50, 'affinity': 50, 'msg': ['Engineer can be on call but would rather not']}, {'name': 'Jamsin', 'yn': 16, 'skill': 40, 'affinity': 50, 'msg': ['Engineer can be on call but would rather not']}, {'name': 'chros', 'yn': 16, 'skill': 30, 'affinity': 20, 'msg': ['Engineer can be on call but would rather not']}]

#creates csv file
csv_columns = ['name', 'yn', 'skill', 'affinity', 'msg']
csv_file = "names.csv"
try:
    with open(csv_file, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for data in dict_data:
            writer.writerow(data)
except IOError:
    print("I/O error")

#reads csv file
with open('names.csv', 'r') as file:
    csv_reader = csv.reader(file, delimiter=',')
    line_count = 0
    a = []
    for row in csv_reader:
        a.append (row)
        print('{row[0]} {row[1]} {row[2]}')
        line_count += 1
    print('Processed {line_count} lines.')
    #print(a)

values = {"values": a}
chartID='1ilBIlml-upQDmV1IRRjxC-74_GxWjuGHnXlqJRqU8bY'

result = service.spreadsheets().values().update(
    spreadsheetId=chartID, range='A1:Z32',
    valueInputOption='USER_ENTERED', body=values).execute()
print('{0} cells updated.'.format(result.get('updatedCells')))
