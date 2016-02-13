from xml.dom import minidom
import urllib
import os

i=0
url = 'http://shop.doverstreetmarket.com/sitemap.xml'
xml = urllib.urlopen(url).read()
xmldoc = minidom.parseString(xml)

loc_values = xmldoc.getElementsByTagName('loc')

# prints the first loc it finds
#print loc_values[0].firstChild.nodeValue


# prints all loc in the XML doc
for loc_val in loc_values:

    print "\nloc[" + str(i) + "] :: \n" + loc_val.firstChild.nodeValue
    i+=1

print "\n"

