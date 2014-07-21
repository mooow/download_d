# download_d Copyright © 2014 Lorenzo Mureu <mureulor@gmail.com>
# 
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
# 

print("download_d Copyright © 2014 Lorenzo Mureu <mureulor@gmail.com>\n\n\n")

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
imgs = doc.findall(".//img");

print("{0} images found".format(len(imgs)))
for img in imgs:
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
