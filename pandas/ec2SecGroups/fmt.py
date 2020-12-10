#!/usr/bin/env python
import sys
import pandas as pd
import json
# Create dataframe
data = pd.read_json('ec2_data.json')
df=data.drop(columns='sec_groups')

def doSQL():
    # Create column list
    cols = "`,`".join([str(i) for i in df.columns.tolist()])
    print("Columns in DB: "+cols)
    # Insert dataframe records
    for i,row in df.iterrows():
        sql = "INSERT IGNORE INTO `ec2` (`" +cols + "`) VALUES (" + "%s,"*(len(row)-1) + "%s)"
        print(sql, tuple(row))

def doData():
    sg=data[['instance_id','sec_groups']]
    a=[]
    for x in sg.values:
        for y in x[1]:
            b=dict()
            b={"instance_id": x[0]}
            b.update(y)
            a.append(b)
    df2=pd.DataFrame.from_dict(a)
    print(df2)
#doSQL()
doData()
