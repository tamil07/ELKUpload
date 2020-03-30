#import requests, json, os, subprocess
#Adding a comment
import json
import os
import subprocess
import requests
from elasticsearch import Elasticsearch
aa='curl http://vmax-jenkins01.cec.lab.emc.com:8080/view/gos-builds/job/gos-foxtail-snapshot/'
bb='/api/json'
cc='>> /root/gos-foxtail-snapshot/'
dd='.json'
for i in range(1,400):
    line=aa+str(i)+bb+cc+str(i)+dd
    sut=subprocess.Popen(line, stderr=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
    sut1=sut.communicate()
    if sut.wait()!=0:
        print ("Failed")
    else:
        print ("Success")
for inp in os.listdir('/root/gos-foxtail-snapshot/'):
    f = open('/root/gos-foxtail-snapshot1/'+inp, 'w')
    print(f)
    f1 = open('/root/gos-foxtail-snapshot/'+inp, 'r')
    print(f1)
    data = json.load(f1)
    f.write(json.dumps(data, indent=1))
    f.close()
directory='/root/gos-foxtail-snapshot1/'
res=requests.get('http://10.118.252.94:9200')
print(res.content)
es=Elasticsearch([{'host':'10.118.252.94','port':'9200'}])
i=1
for filename in os.listdir(directory):
    f=open('/root/gos-foxtail-snapshot1/'+filename)
    docket_content=f.read()
    print(filename)
    try:
        es.index(index='myindex1',ignore=400,doc_type='docket',id=i,body=json.loads(docket_content))
    except:
        print("There is an issue with the filename",filename)
    i+=1
