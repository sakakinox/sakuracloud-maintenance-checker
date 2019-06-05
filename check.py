#!/usr/bin/python3
import sys
import os
import json
import toml
import requests

if (os.path.exists("/usr/local/src/sakuracloud-maintenance-checker/config.toml")!=1):
    print (2)
    sys.exit ("config.tomlがありません。")

config = toml.load(open("/usr/local/src/sakuracloud-maintenance-checker/config.toml"))
if (len(sys.argv)<2):
    print(2)
    sys.exit ("引数が足りません。")

serverid = sys.argv[1]
if (serverid == ""):
    print (2)
    sys.exit ("serveridが設定されていません。")
print (serverid)
sys.exit

apikey = config["API"]["key"]
apisecret = config["API"]["secret"]
url = config["API"]["url"]

r = requests.get(url+serverid, auth=(apikey,apisecret))
results = json.loads(r.text)

host_url = results["Server"]["Instance"]["Host"]["InfoURL"]

if(host_url !=""):
    print (1)
else :
    print (0)

