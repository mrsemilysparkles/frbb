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

if len(sys.argv) < 2:
    print("usage: {} <file>".format(sys.argv[0]))
    sys.exit(0)


file = sys.argv[1]
plural_nouns = 0 
nouns = 0
print("File: {}".format(file))

from frbb.models import Word
for line in open(file,'r').readlines():
    text = line.strip()
    if text.endswith('s'):
	word = Word.objects.create(word=text, category='pn')
    	plural_nouns +=1
    else:
      word = Word.objects.create(word=line.strip(), category='n')
      nouns +=1

    word.save()

print("Loaded {} plural nouns into database".format(plural_nouns))
print("Loaded {} nouns into database".format(nouns))

