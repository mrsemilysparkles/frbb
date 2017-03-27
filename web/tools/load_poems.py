#!/usr/bin/python
import os
import sys
import csv


## DJANGO SETUP
##
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'flipside.settings')
import django
django.setup()
##
##

def add_poem(poem):
    ascii_only_text = str(poem).encode('ascii', errors='ignore')
    p = Poem.objects.create(text=ascii_only_text, category='r')
    p.withdrawn = False
#    print(p)
    p.save()
    return p



if len(sys.argv) < 2:
    print("usage: {} <file>".format(sys.argv[0]))
    sys.exit(0)


file = sys.argv[1]
poems = 0
print("File: {}".format(file))


from frbb.models import Poem
for row in csv.reader(open(file,'r')):
    add_poem(row[1])
    poems += 1

print("Loaded {} poems into database".format(poems))





#if __name__ =='__main__':
#    for row in csv.reader(f):
#        add_poem(row[2])
#
#    for p in Poem.objects.all():
#        print p

