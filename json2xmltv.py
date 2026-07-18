import requests, json
from datetime import datetime, timedelta

r = requests.get('https://meta.metacast.eu/?radio=radioenergy&songsNumber=3', headers={'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'accept-language': 'en-US;q=0.8,en;q=0.7'})
fileName="radioenergy.xml"

def specChar(str):
    if str is None:
        return ""
    str=str.replace('"', '&quot;')
    str=str.replace("'", '&apos;')
    str=str.replace('<', '&lt;')
    str=str.replace('>', '&gt;')
    str=str.replace('&', '&amp;')
    return str

def writeData(js=""):
    if js["time"] is None:
        return
    date = datetime.fromisoformat(js["time"])
    duration = datetime.strptime(js["duration"], '%H:%M:%S')
    with open(fileName, "a") as f:
        f.write('<programme start="'+date.strftime('%Y%m%d%H%M%S')+' +0300" stop="'+(date+timedelta(minutes=duration.minute, seconds=duration.second)).strftime('%Y%m%d%H%M%S')+' +0300" channel="radioenergy">\n')
        f.write('<title>'+specChar(js["title"])+'</title>\n')
        f.write('<sub-title>\n'+specChar(js["artist"])+'\n</sub-title>\n')
        f.write('<image type="poster">'+specChar(js["image"])+'</image>\n')
        f.write('</programme>\n')

if r.status_code==200:
    with open(fileName, "w") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n<!DOCTYPE tv SYSTEM "xmltv.dtd">\n\n')

    with open(fileName, "a") as f:
        f.write('<tv generator-info-name="Jir_14 json2xmltv" source-info="'+specChar("https://meta.metacast.eu/?radio=radioenergy&songsNumber=3")+'">\n')
        f.write('<channel id="radioenergy">\n<display-name>Radio ENERGY</display-name>\n</channel>\n')
    
    js = json.loads(r.content)
    for section in js:
        if section=="history":
            for rec in js[section]:
                writeData(js=rec)
        else:
            writeData(js=js[section])
            
    with open(fileName, "a") as f:
        f.write('</tv>')
else:
    print("Error catching data")