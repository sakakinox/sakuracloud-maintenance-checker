#!/usr/bin/python3
import sys
import json
import requests

apikey = ""
apisecret = ""
url = ""

if(apikey == "" or apisecret == "" or url == ""):
    sys.exit("API key not exist.")

def get_json (url,key,secret):
    r = requests.get(url, auth=(key,secret))
    if(r.status_code != 200):
        sys.exit("API server error "+ str(r.status_code ))

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

results = get_json(url+"server/",apikey,apisecret)
print (get_infourl(results,ipaddr))
