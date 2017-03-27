#!/usr/bin/python
import os
import sys


## DJANGO SETUP
##
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'flipside.settings')
import django
django.setup()
##
##

if len(sys.argv) < 3:
    print("usage: {} <file> <format>".format(sys.argv[0]))
    sys.exit(0)


file = sys.argv[1]
format = sys.argv[2]
words = 0 
print("File: {}, Format: {}".format(file,format))

from frbb.models import Word
for line in open(file,'r').readlines():
    word = Word.objects.create(word=line.strip(), category=format)
    word.save()
    words += 1

print("Loaded {} words into database".format(words))

