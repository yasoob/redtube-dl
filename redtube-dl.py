import urllib2
import re
import sys
try:
    try:
        url = sys.argv[1]
    except IndexError:
        url = raw_input("[redtube]  which file do you want to download?          ")
    if "http" not in url:
        url = "http://"+ url
    if "redtube.com" not in url:
        print "[redtube]  invalid url"
        sys.exit()
    print "[redtube]  got the url"
    print "[redtube]  loading webpage"
    html = urllib2.urlopen(url).read()
    print "[redtube]  page loaded"
    line = re.sub("%22",'"',html)
    line = re.sub("%7D","}",line)
    line = re.sub("%2C",",",line)
    line = re.sub("%7B","{",line)
    line = re.sub("%3A",":",line)
    line = re.sub("%5D","]",line)
    line = re.sub("%2F","/",line)
    line = re.sub("%5C","",line)
    line = re.sub("%3F","?",line)
    line = re.sub("%3D","=",line)
    line = re.sub("%2B","+",line)
    line = re.sub("%25","%",line)
    line = re.sub("%3E",">",line)
    line = re.sub("%3C","<",line)
    abc = re.search(r"src=\'" + "http:" + r"(.+?)'", line)
    print "[redtube]  " +"http:"+ abc.group(1)
except urllib2.URLError:
    print "[redtube]  invalid url"
    sys.exit()
