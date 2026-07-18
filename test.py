import requests
from datetime import datetime, timedelta

r = requests.get('https://api.instant.audio/data/playlist/76/energy')
fileName="radioenergy.xml"

json = r.json()
if json["success"]:
    with open(fileName, "w") as f:
        f.write('<tv generator-info-name="Jir_14 json2xmltv" source-info="https://api.instant.audio/data/playlist/76/energy">\n')
    with open(fileName, "a") as f:
        f.write('<channel id="radioenergy">\n<display-name>Radio ENERGY</display-name>\n</channel>\n')
    res=json["result"]
    time=datetime.now()
    for r in res:
        time2=time+timedelta(minutes=3)
        with open(fileName, "a") as f:
            f.write('<programme start="'+time.strftime('%Y%m%d%H%M%S')+' +0000" stop="'+time2.strftime('%Y%m%d%H%M%S')+' +0000" channel="radioenergy">\n')
            f.write('<title>'+r["track_title"]+'</title>\n')
            f.write('<sub-title>\n'+r["track_artist"]+'\n</sub-title>\n')
            f.write('<image type="poster">'+r["track_image"]+'</image>\n')
            f.write('</programme>\n')
        time=time2