#!/bin/python
import os, json, subprocess, time
from datetime import datetime

WAIT=15
COMMAND_DUMP='mysqldump --host={0} --port={1} --user={2} --protocol=tcp --skip-triggers --default-character-set=utf8 --password={3} {4} > {5}'
def mysql_dump(json):
    print({'message' : 'DUMP DATA BASE MYSQL'})
    json_log = json
    print({'message' : 'LOAD DATA', 'data': json_log})
    hostname = json['hostname']
    port = json['port']
    username = json['username']
    password = json['password']
    folderpath = json['folderpath']
    foldername = json['foldername']
    database = json['database']
    folderfullpath = os.path.join(folderpath, foldername)
    exists_folder = os.path.isdir(folderfullpath)
    if exists_folder == False:
        print('create folder -> ', folderfullpath)
        os.makedirs(folderfullpath) 
    now = datetime.now()
    filename = now.strftime("%Y%m%d_%H%M%S") + '.sql'
    fullpathname = os.path.join(folderfullpath, filename)
    print({'message' : 'CREATE DUMP'})
    COMMAND_EXEC = COMMAND_DUMP.format(hostname, port, username, password, database, fullpathname)
    COMMAND_DUMP_LOG = COMMAND_DUMP.format(hostname, port, username, 'XXXXXXX', database, fullpathname)
    print({'message' : 'COMMAND EXECUTE', 'command': COMMAND_DUMP_LOG})
    p = subprocess.Popen(COMMAND_EXEC, shell=True)
    print({'message' : p })
    time.sleep(WAIT)
    print({'message' : 'COMMAND EXECUTE', 'command': 'ls'})
    print({'message' : os.listdir(folderfullpath) })
