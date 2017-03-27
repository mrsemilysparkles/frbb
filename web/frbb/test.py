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

from printer import print_poem
poem="""Stamens are lovely; saps are of a daffodil hue. Drake is foolish. May I watch Showgirls with you?"""
print_poem(poem) 
