#!/usr/bin/python3

import urllib.request as u
from urllib.error import URLError
import os
import time

 # clone the app, install deps:

os.system('clear')
os.system('git clone https://github.com/bigpandaio/ops-exercise.git')
os.system('mv ops-exercise/* .')
os.system('npm install')
print("+ repo cloned, deps installed.")

 # get the image files:

file = u.urlretrieve("https://s3.eu-central-1.amazonaws.com/devops-exercise/pandapics.tar.gz", "pandapics.tar.gz")
path = "public/images"
os.system('mkdir ' +path)
os.system('tar -zxvf ' +file[0] + ' -C ' +path)
os.system('rm -f ' +file[0])
os.system('clear')
print("+ images added to directory.")

 # launch the app:

os.system('docker-compose up -d')
print('+ Launching app...')
time.sleep(5)

 # healthcheck:

#req = u.Request('http://localhost:3000')

while True:
    try: 
        req = u.Request('http://localhost:3000')
        u.urlopen(req)
        print('+ BP app is running :)')
        time.sleep(3)
    except URLError as e:
        print('Service down: ', e.reason)
        time.sleep(3)
        os.system('docker-compose down')
        break

