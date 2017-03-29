#!/usr/bin/env python

import urllib, urllib2
import json
import time
import codecs

# Change these parameters to reflect the files and fields you're working with. Add relevant fields if working with a csv.
inFile = 'dKwordsApp.txt' #modify
sep = ','
keywordField = 'keyword'
outFile = 'dKwordsAppAutoComp.txt' #modify

# This is the URL that you're getting your json data from in the query_google function below.
google_endpoint = 'http://google.com/complete/search?output=firefox&q='

# Finds the index for your csv file. Not as relevant here but I kept it in to facilitate scaling the code.
def find_index(fieldname, inFile):
    with open(inFile, 'r') as f:
        header = f.readline().rstrip().split(sep)
        i = 0
        for i in range(0, len(header)):
            if header[i] == fieldname:
                return i
                break
        else:
            return -1

# Modify the phrase parameters to get your url string.
# Prompts: 'why did', 'how did', 'when did', 'why was', 'contrast %s and', 'history of'
def build_phrase(keyword):
    phrase = u'history of'    # Depending on sentence structure, you may need to add a %s string in this variable, as well as a % (keyword)  
    return u'%s %s' % (phrase, keyword)

# This is where you build your keyword phrase, request the json data with autocomplete strings, and then return the json data as data.
def query_google(phrase):
    url = '%s%s' % (google_endpoint, urllib.quote_plus(phrase))
    data = urllib2.urlopen(url)
    data = json.load(data)
    results = data[1]
    return results

kwIndex = find_index(keywordField, inFile)

# Then we get down to writing.
with codecs.open(inFile, 'r', 'utf-8') as f:
    with codecs.open(outFile, 'a', 'utf-8') as f_out:     
        data = f.readlines()
        for record in data[1:]:
            time.sleep(0.3)
            
            record = record.rstrip()
            items = record.split(sep)
            kw = items[kwIndex]
                
            phrase = build_phrase(kw)
            results = query_google(phrase)
            if len(results) > 0:
                for result in results:
                    f_out.write('%s, %s, %s\n' % (kw, phrase, result))
            else:
                f_out.write('%s, %s, no autocomplete results\n' % (kw, phrase))