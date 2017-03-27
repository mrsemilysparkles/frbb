
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'flipside.settings')
import django
django.setup()


from frbb.models import Word

#for word in Word.objects.all():
#    print("{}, category={}".format(word.word, word.category))

Word.objects.filter(category='n').delete()
