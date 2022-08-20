#!/bin/python
import os, json, subprocess
from datetime import datetime

COMMAND_DUMP='mysqldump -h {0} --port {1} -u {2} --password={3} {4} > {5}'

def mysql_dump(json):
    print({'message' : 'DUMP DATA BASE MYSQL'})
    json_log = json
    json_log['password'] = 'XXXXXXXXXX'
    print({'message' : 'LOAD DATA', 'data': json_log})
    hostname = json['hostname']
    port = json['port']
    username = json['username']
    password = json['password']
    folderpath = json['folderpath']
    foldername = json['foldername']
    database = json['database']
    now = datetime.now()
    filename = now.strftime("%Y%m%d_%H%M%S") + '.sql'
    fullpathname = os.path.join(folderpath, foldername, filename)
    print({'message' : 'CREATE DUMP'})
    COMMAND_EXEC = COMMAND_DUMP.format(hostname, port, username, password, database, fullpathname)
    COMMAND_DUMP_LOG = COMMAND_DUMP.format(hostname, port, username, 'XXXXXXX', database, fullpathname)
    print({'message' : 'COMMAND EXECUTE', 'command': COMMAND_DUMP_LOG})
    p = subprocess.Popen(COMMAND_EXEC, stdout=subprocess.PIPE, shell=True)
    print({'message' : p })
