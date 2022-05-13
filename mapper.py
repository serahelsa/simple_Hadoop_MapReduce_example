#!/usr/bin/env python
import sys

# get all lines from stdin
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # split the line into words; splits on any whitespace
    words = line.split()

    # stopwords_punctuation set
    #stopwords_punch = set(['the','and','!','(',')','-','[',']','{','}',';',':','"','\',',','<','>','.','/','?','@','#','$','%','^','&','*','_','~'])
    stopwords_punch = set(['the','and','!','(',')','-','[',']','{','}'])

    # output tuples (word, 1) in tab-delimited format
    for word in words:
        if word not in stopwords_punch:
            print '%s\t%s' % (word, "1")
