
import django_rq
import redis

def new_account_lighting():
    r = redis.Redis()
    r.publish('light', 'new_account')

def deposit_lighting():
    r = redis.Redis()
    r.publish('light', 'deposit')

def withdraw_lighting():
    r = redis.Redis()
    r.publish('light', 'withdraw')

def logout_lighting():
    r = redis.Redis()
    r.publish('light', 'logout')

def out_of_paper_lighting():
    r = redis.Redis()
    r.publish('light', 'paper')

def login_lighting():
    r = redis.Redis()
    r.publish('light','login')
