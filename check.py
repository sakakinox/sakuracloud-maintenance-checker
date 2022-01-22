#!/usr/bin/env python3
import sys
import json
import requests

apikey = "ho"
apisecret = "jo"
url = " "

if(apikey == "" or apisecret == "" or url == ""):
    sys.exit("API key not exist.")

def get_json (url,key,secret):
    try: 
        r = requests.get(url, auth=(key,secret))
    except requests.exceptions.MissingSchema :
        sys.exit("Get JSON error")
    if(r.status_code != 200):
        sys.exit("API server error "+ str(r.status_code ))
    result = json.loads(r.text)
    return(result)

def get_infourl (json,ip,infourl = ""):
    for server in json["Servers"]:
        for interface in server["Interfaces"]:
            if interface["IPAddress"]==ip or interface["UserIPAddress"]==ip:
                try:
                    infourl = server["Instance"]["Host"]["InfoURL"]
                except TypeError as e:
                    return "Type Error (server may be powered off)"
                if not infourl:
                    return "0"
                else:
                    return(infourl)

    return "ip address not found"

if (len(sys.argv)<2):
    print(2)
    sys.exit ("引数が足りません。")

ipaddr = sys.argv[1]
if (ipaddr == ""):
    sys.exit ("ipアドレスが設定されていません。")

results = get_json(url,apikey,apisecret)

print (get_infourl(results,ipaddr))