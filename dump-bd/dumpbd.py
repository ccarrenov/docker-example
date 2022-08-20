#!/bin/python
import json
from db.mysql import mysqldb
from db.postgresql import postgresqldb

f = open('connection.json')
datajson = json.load(f)
  
for data in datajson:
    if data['engine'] == 'mysql':
        mysqldb.mysql_dump(data['data'])
    if data['engine'] == 'postgresql':
        postgresqldb.mysql_dump(data['data'])        
f.close()
