import sys
import json

ipDict = {}
countFrequency = {}
timeInterval = int(sys.argv[1])
for line in sys.stdin:
    if len(line) < 10:
        continue
    data = json.loads(line)
    domain = data["name"]
    if domain not in ipDict.keys():
        ipDict[domain] = {}
        countFrequency[domain] = 0
    else:
        if data["status"] == "NOERROR":
            if data["data"]["ipv4_addresses"][0] not in ipDict[domain].keys():
                countFrequency[domain] += 1
        else:
            if len(ipDict[domain]) > 0:
                countFrequency[domain] += 1
    ipDict[domain] = {}
    if data["status"] == "NOERROR":
        for ip in data["data"]["ipv4_addresses"]:
            ipDict[domain][ip] = 1

sorted_list = sorted(countFrequency.items(), key=lambda x: x[1], reverse=True)
for data in sorted_list:
    if (float(data[1]) == 0.0):
        print(timeInterval*2)
    else:
        print(timeInterval/float(data[1]))
