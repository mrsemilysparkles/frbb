from __future__ import unicode_literals

import uuid
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Poem(models.Model):
    CATEGORIES = ( ('c', 'consent'), ('r', 'random'), )
    created = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    uuid = models.UUIDField(editable=False, unique=True, default=uuid.uuid4)
    withdrawn = models.BooleanField(default=0)
    category = models.CharField(max_length=2, choices=CATEGORIES)
    def __unicode__(self):
       return '{"uuid":"%s","text":"%s"}' % (self.uuid, self.text)


class UserProfile(models.Model):
    # Links the UserProfile to a User model instance.
    user = models.OneToOneField(User)
    created = models.DateTimeField(auto_now_add=True)
    uuid = models.UUIDField(editable=False, unique=True, default=uuid.uuid4)
    login_count = models.IntegerField(default=0)
    withdrawn = models.IntegerField(default=0)
    balance = models.IntegerField(default=5)
    poems = models.ManyToManyField(Poem, blank=True)

    def __unicode__(self):
        return '{"user":"%s","balance":"%s"}' % (self.user, self.balance)

class Word(models.Model):
    #Contains all the words used for poem mad libs
    CATEGORIES = ( ('pn', 'plural-noun'), ('n','noun'),('c','color'),
                  ('v','verb'), ('a','adjective'), )

    uuid = models.UUIDField(editable=False, unique=True, default=uuid.uuid4)

    word = models.CharField(max_length=30)
    category = models.CharField(max_length=2, choices=CATEGORIES)

    def __unicode__(self):
        return '{"word": "%s", "category": "%s"}' % (self.word, self.category)

