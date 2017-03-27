import csv
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'flipside.settings')
import django
django.setup()

from frbb.models import Poem
f = open('database/poetry.csv')

def add_poem(poem):
    p = Poem.objects.create(text=poem)
    p.withdrawn= False
    p.save()
    return p



if __name__ =='__main__':
    for row in csv.reader(f):
        add_poem(row[2])

    for p in Poem.objects.all():
        print p

