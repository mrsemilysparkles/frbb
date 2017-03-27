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
colors = 0 
print("File: {}".format(file))

from frbb.models import Word
for line in open('database/colors.csv','r').readlines():
    values = line.split(',')
    color = values[0]
    color = color.replace('_', ' ')
    word = Word.objects.create(word=color, category='c')
    word.save() 
    colors +=1

print("Loaded {} colors into database".format(plural_nouns))

