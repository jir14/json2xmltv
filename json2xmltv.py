import requests, json
from datetime import datetime, timedelta

r = requests.get('https://meta.metacast.eu/?radio=radioenergy&songsNumber=3', headers={'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',  'accept-language': 'cs,sk;q=0.9,en-US;q=0.8,en;q=0.7'})
fileName="radioenergy.xml"

#r=b'\xef\xbb\xbf{"prev_song":{"id":"3147","image":"https:\\/\\/lastfm.freetls.fastly.net\\/i\\/u\\/174s\\/83c7f7013abd4e48b4723114c8ceb966.png","artist":"AGNES","title":"Release Me","duration":"00:03:04","time":"2026-07-18T14:48:44+03:00"},"current_song":{"id":"1693","image":"https:\\/\\/lastfm.freetls.fastly.net\\/i\\/u\\/174s\\/c54ef969134a491e8b6cca3c171dee44.png","artist":"DJ BOBO","title":"Shadows Of The Night","duration":"00:04:19","time":"2026-07-18T14:51:54+03:00"},"next_song":{"id":"77432","image":"https:\\/\\/is1-ssl.mzstatic.com\\/image\\/thumb\\/Music211\\/v4\\/7a\\/7a\\/d2\\/7a7ad2c3-a95e-d19d-dc59-28b9a0769e05\\/199316517163_cover.jpg\\/360x360bb.jpg","artist":"BEBE REXHA & FAITHLESS","title":"New Religion","duration":"00:02:52","time":"2026-07-18T14:56:18+03:00"},"history":[{"id":"70700","image":"https:\\/\\/is1-ssl.mzstatic.com\\/image\\/thumb\\/Music221\\/v4\\/07\\/38\\/6a\\/07386aaa-d1b6-322d-1563-714a9c365c36\\/artwork.jpg\\/360x360bb.jpg","artist":"ARGY FT. OMNYA","title":"Aria","duration":"00:02:31","time":"2026-07-18T14:46:14+03:00"},{"id":"718","image":"https:\\/\\/lastfm.freetls.fastly.net\\/i\\/u\\/174s\\/e0b586474b261ae74086b2fe7ea1eafa.png","artist":"ROBERT MILES","title":"Children","duration":"00:03:49","time":"2026-07-18T14:42:21+03:00"},{"id":"1227","image":"https:\\/\\/media.metacast.eu\\/pictures\\/11_2023\\/YJh4sVclGtvqFjnrkMdg-92346.jpg","artist":"ANISE K FT. SNOOP DOGG & BELLA BLUE","title":"Walking On Air","duration":"00:03:45","time":"2026-07-18T14:38:28+03:00"},{"id":"1447","image":"https:\\/\\/lastfm.freetls.fastly.net\\/i\\/u\\/174s\\/d449e6306f3b095ed43fbacb2852fb48.png","artist":"MODERN TALKING","title":"No Face No Name No Number","duration":"00:03:40","time":"2026-07-18T14:34:41+03:00"},{"id":"78098","image":"https:\\/\\/is1-ssl.mzstatic.com\\/image\\/thumb\\/Music221\\/v4\\/f2\\/ec\\/c5\\/f2ecc5b1-e88c-3330-e58d-aa0c32a3c0cd\\/26UMGIM14086.rgb.jpg\\/360x360bb.jpg","artist":"ANTIGONI","title":"Jalla","duration":"00:02:59","time":"2026-07-18T14:28:00+03:00"},{"id":"40876","image":"https:\\/\\/is4-ssl.mzstatic.com\\/image\\/thumb\\/Music118\\/v4\\/7d\\/f6\\/5f\\/7df65f39-b657-1ce9-3efb-2191b7f048c8\\/source\\/360x360bb.jpg","artist":"BLACK EYED PEAS","title":"Don\'t Phunk With My Heart","duration":"00:03:41","time":"2026-07-18T14:24:17+03:00"},{"id":"3669","image":null,"artist":"QUAD CITY DJ\'S","title":"Space Jam","duration":"00:04:39","time":"2026-07-18T14:20:46+03:00"},{"id":"65540","image":"https:\\/\\/is1-ssl.mzstatic.com\\/image\\/thumb\\/Music116\\/v4\\/e8\\/dc\\/bc\\/e8dcbc49-c05c-0868-4437-00be6220fa39\\/5054197832710.jpg\\/360x360bb.jpg","artist":"OFENBACH FT. NORMA JEAN MARTINE","title":"Overdrive","duration":"00:02:33","time":"2026-07-18T14:18:08+03:00"},{"id":"4609","image":"https:\\/\\/lastfm.freetls.fastly.net\\/i\\/u\\/174s\\/fc6199250a024120bb35ab99d77bad63.png","artist":"INNA","title":"Hot","duration":"00:03:33","time":"2026-07-18T14:09:47+03:00"},{"id":"1263","image":"https:\\/\\/lastfm.freetls.fastly.net\\/i\\/u\\/174s\\/df8bc7380ef68606d46721cfb0afa8d8.png","artist":"NANA","title":"Let It Rain","duration":"00:03:49","time":"2026-07-18T14:05:59+03:00"}]}'
#r=b'\xef\xbb\xbf{"prev_song":{"id":"13658","image":"https:\\/\\/is5-ssl.mzstatic.com\\/image\\/thumb\\/Music115\\/v4\\/aa\\/07\\/db\\/aa07db20-0b14-d09c-ead7-5b9e3680cb76\\/00602527051840.rgb.jpg\\/360x360bb.jpg","artist":"2PAC FT. DR. DRE","title":"California Love","duration":"00:03:54","time":"2026-07-18T17:00:33+03:00"},"current_song":{"id":"2547","image":"https:\\/\\/lastfm.freetls.fastly.net\\/i\\/u\\/174s\\/1926aeb8879047a89e59578cdb143ddb.png","artist":"DADDY YANKEE","title":"Gasolina","duration":"00:02:49","time":"2026-07-18T17:04:17+03:00"},"next_song":{"id":"3094","image":"https:\\/\\/lastfm.freetls.fastly.net\\/i\\/u\\/174s\\/1dfedc88fd88860511813b2be9eddd17.png","artist":"BRITNEY SPEARS","title":"Born To Make You Happy","duration":"00:04:00","time":"2026-07-18T17:07:19+03:00"},"history":[{"id":"76214","image":null,"artist":"ALEX WARREN","title":"Ordinary (ENERGY Rmx)","duration":"00:02:32","time":"2026-07-18T16:57:39+03:00"},{"id":"41572","image":"https:\\/\\/is4-ssl.mzstatic.com\\/image\\/thumb\\/Music128\\/v4\\/1e\\/e5\\/f1\\/1ee5f13d-8211-a19b-354e-4cac5d017839\\/source\\/360x360bb.jpg","artist":"BEAT SYSTEM","title":"What\'s Going On (In Your Mind)","duration":"00:03:48","time":"2026-07-18T16:53:45+03:00"},{"id":"1437","image":"https:\\/\\/lastfm.freetls.fastly.net\\/i\\/u\\/174s\\/b60e110d2d7d0de2db35c47bc20884dc.png","artist":"CRAIG DAVID","title":"Walking Away","duration":"00:02:49","time":"2026-07-18T16:50:57+03:00"},{"id":"59254","image":"https:\\/\\/is3-ssl.mzstatic.com\\/image\\/thumb\\/Music124\\/v4\\/4c\\/8e\\/94\\/4c8e94d4-cdba-ee58-cf6e-d1a55e470954\\/cover.jpg\\/360x360bb.jpg","artist":"DJ MATRIX & MATT JOE FT. CAROLINA MARQUEZ","title":"Sar\\u00e0 Perch\\u00e8 Ti Amo","duration":"00:02:42","time":"2026-07-18T16:48:10+03:00"},{"id":"60184","image":"https:\\/\\/is3-ssl.mzstatic.com\\/image\\/thumb\\/Music5\\/v4\\/3f\\/1d\\/f1\\/3f1df1d2-6b5f-8293-aa6c-f6bfb4053179\\/cover.jpg\\/360x360bb.jpg","artist":"CO.RO. FT. TALEESA","title":"Because The Night","duration":"00:04:18","time":"2026-07-18T16:44:13+03:00"},{"id":"2574","image":"https:\\/\\/lastfm.freetls.fastly.net\\/i\\/u\\/174s\\/00c8215e20064d51cd749015a168f4dd.png","artist":"ELA ROSE","title":"Lovely Words","duration":"00:03:28","time":"2026-07-18T16:40:37+03:00"},{"id":"693","image":null,"artist":"2 4 FAMILY","title":"Stay","duration":"00:03:48","time":"2026-07-18T16:37:09+03:00"},{"id":"74538","image":"https:\\/\\/is1-ssl.mzstatic.com\\/image\\/thumb\\/Music221\\/v4\\/07\\/b4\\/b0\\/07b4b003-96a1-7b2c-1d5b-f683267f85c1\\/cover.jpg\\/360x360bb.jpg","artist":"ELENI FOUREIRA","title":"Disco-Tech","duration":"00:03:18","time":"2026-07-18T16:29:36+03:00"},{"id":"42898","image":"https:\\/\\/is5-ssl.mzstatic.com\\/image\\/thumb\\/Music124\\/v4\\/2b\\/8f\\/62\\/2b8f62cb-5d0c-d288-5fe3-c64a9cdddfce\\/source\\/360x360bb.jpg","artist":"SUMMERLOVE","title":"Remember (Na Na Na Hey Hey)","duration":"00:03:39","time":"2026-07-18T16:25:50+03:00"},{"id":"1099","image":"https:\\/\\/lastfm.freetls.fastly.net\\/i\\/u\\/174s\\/387c34eee53445dc958e1dbe26ab7e52.png","artist":"NANA","title":"Lonely","duration":"00:03:47","time":"2026-07-18T16:22:01+03:00"}]}'

#print(r.content)

def specChar(str):
    if str is None:
        return ""
    str=str.replace('"', '&quot;')
    str=str.replace("'", '&apos;')
    str=str.replace('<', '&lt;')
    str=str.replace('>', '&gt;')
    str=str.replace('&', '&amp;')
    return str

def writeData(js="", key=""):
    print(js)
    date = datetime.fromisoformat(js["time"])
    duration = datetime.strptime(js["duration"], '%H:%M:%S')
    with open(fileName, "a") as f:
        f.write('<programme start="'+date.strftime('%Y%m%d%H%M%S')+' +0300" stop="'+(date+timedelta(minutes=duration.minute, seconds=duration.second)).strftime('%Y%m%d%H%M%S')+' +0300" channel="radioenergy">\n')
        f.write('<title>'+specChar(js["title"])+'</title>\n')
        f.write('<sub-title>\n'+specChar(js["artist"])+'\n</sub-title>\n')
        f.write('<image type="poster">'+specChar(js["image"])+'</image>\n')
        f.write('</programme>\n')


#if True:
if r.status_code==200:
    with open(fileName, "w") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n<!DOCTYPE tv SYSTEM "xmltv.dtd">\n\n')

    with open(fileName, "a") as f:
        f.write('<tv generator-info-name="Jir_14 json2xmltv" source-info="'+specChar("https://meta.metacast.eu/?radio=radioenergy&songsNumber=3")+'">\n')
        f.write('<channel id="radioenergy">\n<display-name>Radio ENERGY</display-name>\n</channel>\n')
    
    #js = json.loads(r)
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
    print("Erro catching data")