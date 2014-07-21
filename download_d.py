import os, lxml.html, urllib.request as request


pdir = os.getenv("HOME") or os.getenv("HOMEPATH")
print("HOME: " + pdir)
ddir = os.path.join(pdir, "download_d")
os.makedirs(ddir, exist_ok=True)
print("Files saved in: " + ddir)

# load html page
URL_IMAGES=r'http://www.diochan.com/d/img.php?x=0&y=0&w=1000&h=1000&z=0'
URL_BASE = r'http://www.diochan.com/d/'
o = request.urlopen(URL_IMAGES)
# load DOM
doc = lxml.html.document_fromstring(o.readall().decode())
# search all <img> tags
for img in doc.findall(".//img"):
    url = URL_BASE + img.attrib["src"] # img url
    bn = img.attrib["id"]              # file name
    fp = os.path.join(ddir, bn)        # file path

    print ( "[{0}]...".format(fp))
    
    # download and save
    f = open(fp, "wb")
    o = request.urlopen(url)
    f.write(o.read())
    f.close()
    print(".\n")
print("Done.")
