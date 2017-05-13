import urllib.request
import xml.etree.ElementTree as etree
from collections import OrderedDict
import re
from datetime import datetime
from dateutil.relativedelta import relativedelta
import dateparser


def countdigits(string, sym_count={}):
    for sym in string:
        if not sym in sym_count:
            sym_count[sym] = 1
        else:
            sym_count[sym] += 1

    return(sym_count)


def printdigits(sym_count):
    sym_sorted = OrderedDict(sorted(sym_count.items()))

    for sym in sym_sorted.keys():
        print(sym+','+str(sym_sorted[sym]))


def gettimestamp(dt_string):

    '''
    months = 0
    days = 0
    hours = 0
    mins = 0

    search = re.search("(\d+)\s+?month", dt_string)
    if search:
        months = int(search.group(1))

    search = re.search("(\d+)\s+?day", dt_string)
    if search:
        days = int(search.group(1))

    search = re.search("(\d+)\s+?hour", dt_string)
    if search:
        hours = int(search.group(1))

    search = re.search("(\d+)\s+?minute", dt_string)
    if search:
        mins = int(search.group(1))

    timestamp = datetime.now() - relativedelta(months=months, days=days,hours=hours,minutes=mins)
    '''
    timestamp = dateparser.parse(dt_string)

    return(int(timestamp.timestamp()))


def getbeacon(tm):
    response = urllib.request.urlopen("https://beacon.nist.gov/rest/record/"+str(tm))
    xml_resp = response.read()
    tree = etree.ElementTree(etree.fromstring(xml_resp))
    output = etree.ElementTree(tree.find('{http://beacon.nist.gov/record/0.1/}outputValue'))
    text = output.getroot().text

    return(text)


def getlastbeacon():
    response = urllib.request.urlopen("https://beacon.nist.gov/rest/record/last")
    xml_resp = response.read()
    tree = etree.ElementTree(etree.fromstring(xml_resp))
    output = etree.ElementTree(tree.find('{http://beacon.nist.gov/record/0.1/}outputValue'))
    text = output.getroot().text

    return(text)
