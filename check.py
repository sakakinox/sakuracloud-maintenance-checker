#!/usr/bin/env python3
import sys
import json
import requests

# url = https://secure.sakura.ad.jp/cloud/zone/tk1a/api/cloud/1.1/ (東京第1ゾーン)
# url = https://secure.sakura.ad.jp/cloud/zone/tk1b/api/cloud/1.1/ (東京第2ゾーン)
# url = https://secure.sakura.ad.jp/cloud/zone/is1a/api/cloud/1.1/ (石狩第1ゾーン)
# url = https://secure.sakura.ad.jp/cloud/zone/is1b/api/cloud/1.1/ (石狩第2ゾーン)
# url = https://secure.sakura.ad.jp/cloud/zone/tk1v/api/cloud/1.1/ (Sandbox)

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
    for server in json["Servers"]:
        for interface in server["Interfaces"]:
            if interface["IPAddress"]==ip or interface["UserIPAddress"]==ip:
                try:
                    infourl = server["Instance"]["Host"]["InfoURL"]
                except TypeError as e:
                    return "Type Error (server may be powered off)"
#                infourl ="https://test/"
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