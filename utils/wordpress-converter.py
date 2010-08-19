########################
# wp2toto              #
#   by Joseph Weissman #
########################

# config

author = "Mark Borcherding"
wpfile = "../archive/wordpress.backup.xml"
outdir = "../articles/"


import pprint
import time
from time import strftime
import xml.dom.minidom
from xml.dom.minidom import Node

def extract_string(xml_node, tag_name):
  string = ""
  n = xml_node.getElementsByTagName(tag_name)
  for node in n:
    for node2 in node.childNodes:
      # if tag_name == "content:encoded":
      #  print node2.nodeType
      if node2.nodeType == Node.TEXT_NODE or node2.nodeType == Node.CDATA_SECTION_NODE:
        string += node2.data
  return string
  
doc = xml.dom.minidom.parse(wpfile)
wp_date_format   = "%a, %d %b %Y"
toto_date_format = "%y-%m-%d"
for node in doc.getElementsByTagName("item"):
  yaml = ""  
  title   = extract_string(node, "title").replace("/","").replace("  "," ").replace(":"," --")
  date    = extract_string(node, "pubDate")[0:17].strip()
  content = extract_string(node, "content:encoded").strip()
  if not title == "" and not date.endswith("-0001") and not content == "":
    converted_date = time.strftime(toto_date_format, time.strptime(date, wp_date_format) )
    filename = "20"+converted_date+"-"+title.replace(" ","-")+".txt"
    yaml += "title: "+title+"\n"
    yaml += "author: "+author+"\n"
    yaml += "date: 20"+converted_date.replace("-","/")+"\n"   #" ("+date+")\n"
    yaml += "\n\n\n"
    yaml += content +"\n"
    # yaml += "--------------\n\n"
    print yaml
    # filename = "example.dat" # debug
    file = open(outdir+filename.lower(), "w")
    file.writelines(yaml.encode('ascii', 'ignore'))
    file.close()