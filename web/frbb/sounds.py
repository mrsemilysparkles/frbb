
import django_rq
import redis

def new_account_sound():
    r = redis.Redis()
    r.publish('sound', 'new_account')

def deposit_sound():
    r = redis.Redis()
    r.publish('sound', 'deposit')

def withdraw_sound():
    r = redis.Redis()
    r.publish('sound', 'withdraw')

def logout_sound():
    r = redis.Redis()
    r.publish('sound', 'logout')

def login_sound():
    r = redis.Redis()
    r.publish('sound','login')
