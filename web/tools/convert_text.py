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

def update_poem(poem, uuid):
    p = Poem.objects.get(uuid=uuid)
    if p.text != poem:
        print("Poem [{}], has bad characters".format(uuid))
#        p.text = poem
#        p.save()



poems = 0

from frbb.models import Poem
for poem in Poem.objects.all():
    ascii_only_text = poem.text.encode('ascii', 'ignore')
    update_poem(ascii_only_text, poem.uuid)
    poems += 1

print("Converted {} poems in database".format(poems))

