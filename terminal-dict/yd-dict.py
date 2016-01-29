#! /usr/bin/env python 
# -*- coding:utf-8 -*-

from __future__ import unicode_literals
import os
import sys
import getopt
import logging
import urllib2
import json
import re
import string


//good try
url = 'http://fanyi.youdao.com/openapi.do?keyfrom=nosrepus-yd&key=1740281583&type=data&doctype=json&version=1.1&q=' 

logger = logging.getLogger(__name__)

def get_result(words):
    try:
        page = urllib2.urlopen(url + words)
        result=page.read()
    except urllib2.URLError:
        logger.error('wrong')
        return
    return result

def show(data):
    data = json.loads(data)
    errorCode = data.get('errorCode', -1)
    if errorCode != 0:
         print 'Wrong query'
    else: 
         print 'basic meaning:'
         items = data.get('translation',None)
         if items:
             for item in items:
                 print u'\t', item
         print 'web meaning'
         web_items = data.get('web', None)
         if web_items:
             for item in web_items:
                 print item.get('key', None), ':'
                 for v in item.get('value',''):
                     print u'\t\t', v 

def main():
    try:
        options, args = getopt.getopt(sys.argv[1:],["help"])
    except getopt.GetoptError as e:
        pass
    print u''  
    match = re.findall(r'[\w.]+', " ".join(args).lower())
    words = "_".join(match)
    json = get_result(words)
    show(json)

if __name__ == '__main__':
    main()
