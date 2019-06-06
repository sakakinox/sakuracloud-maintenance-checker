#!/usr/bin/python3
import sys
import os
import json
import requests

apikey = ""
apisecret = ""
url = ""

def get_json (url,key,secret):
    r = requests.get(url, auth=(key,secret))
    result = json.loads(r.text)
    return(result)

def get_infourl (json,ip,infourl = ""):
    num = len(json["Servers"])
    for i in range(num):
        instance =json["Servers"][i]

        if (instance["Interfaces"][0]["IPAddress"]==ip):
            infourl = instance["Instance"]["Host"]["InfoURL"]
    return(infourl)



if (len(sys.argv)<2):
    print(2)
    sys.exit ("引数が足りません。")

ipaddr = sys.argv[1]
if (ipaddr == ""):
    sys.exit ("ipアドレスが設定されていません。")
#print (serverid)




results = get_json(url,apikey,apisecret)
#print (json.dumps(results["Servers"][28]["Index"],indent=2))
#print (len(results["Servers"]))
#print (get_instanceid(results,serverid))
print (get_infourl(results,ipaddr))
#host_url = results["Server"]["Instance"]["Host"]["InfoURL"]

#if(host_url !=""):
#    print (1)
#else :
#    print (0)

