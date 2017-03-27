
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'flipside.settings')
import django
django.setup()


from frbb.models import Word
for line in open('nouns.txt','r').readlines():
    #print line.strip()
    word = Word.objects.create(word=line.strip(), category='n')
    word.save() 
