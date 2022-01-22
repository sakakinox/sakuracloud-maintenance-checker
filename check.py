#!/usr/bin/env python3
import sys
import json
import requests

apikey = ""
apisecret = ""
url = ""


def get_json(url, key, secret):
    try:
        r = requests.get(url, auth=(key, secret))
    except requests.exceptions.MissingSchema:
        sys.exit("Http request error.")
    if(r.status_code != 200):
        sys.exit("API server error " + str(r.status_code))
    try:
        result = json.loads(r.text)
    except json.decoder.JSONDecodeError:
        sys.exit("Json format error.")
    return(result)


def get_infourl(dic, ip, isdetect=0, infourl="IP address not detected"):
    for server in dic["Servers"]:
        for interface in server["Interfaces"]:
            if (interface["IPAddress"] == ip or
                    interface["UserIPAddress"] == ip):
                isdetect = isdetect + 1
                try:
                    infourl = server["Instance"]["Host"]["InfoURL"]
                except TypeError:
                    return "Host server error. (server may be powered off)"
    if (isdetect > 1):
        infourl = "Detected multiple servers."
    if (not infourl):
        infourl = "Nothing infomation!"
    return(infourl)


if(apikey == "" or apisecret == "" or url == ""):
    sys.exit("API key not exist.")

if (len(sys.argv) < 2):
    sys.exit("引数が足りません。")

ipaddr = sys.argv[1]
if (ipaddr == ""):
    sys.exit("ipアドレスが設定されていません。")

results = get_json(url+"server", apikey, apisecret)

print(get_infourl(results, ipaddr))
