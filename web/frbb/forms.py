from django import forms
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from .models import UserProfile, Poem, Word
numeric = RegexValidator(r'^[0-9]*$', 'Only numeric characters are allowed.')

class AForm(forms.Form):
    username = forms.CharField(max_length=4, min_length=4)
    username.widget.attrs.update({'autofocus' : 'autofocus', 'autocomplete': 'off', 'class': 'input'})

class BForm(forms.Form):
    password = forms.CharField(max_length=4, min_length=4, 
                               widget=forms.PasswordInput())
    password.widget.attrs.update({'autofocus' : 'autofocus', 'autocomplete': 'off', 'class': 'input'})


class CreateAccountForm(forms.Form):
    account_number = forms.CharField(max_length=4, validators=[numeric])
    account_number.widget.attrs.update({'autofocus':'autofocus', 'autocomplete': 'off', 'class': 'input'})

    def clean_account_number(self):
        print 'Cleaning the account name'
        username = self.cleaned_data['account_number']
        print username
#        if UserProfile.objects.get(user__username=username) is not None:
        if UserProfile.objects.filter(user__username=username).exists():
            raise forms.ValidationError('Account number is not available',
                                        code='invalid') 
        if len(username) is not 4:
            raise forms.ValidationError('Account # must be 4 characters', code='invalid')
        return self.cleaned_data['account_number']

class CreatePinForm(forms.Form):
    pin_number = forms.CharField(max_length=4, validators=[numeric])
    pin_number.widget.attrs.update({'autofocus':'autofocus', 'autocomplete': 'off', 'class':'input'})
    
    def clean_pin_number(self):
        pin_number = self.cleaned_data['pin_number']
        
        if len(pin_number) is not 4:
            raise forms.ValidationError('Pin # must be 4 characters', code='invalid')
        return self.cleaned_data['pin_number']

class WithdrawForm(forms.Form):
    #amount = forms.CharField(max_length=1, validators=[numeric])
    choice = forms.CharField(required=False, max_length=1, widget=forms.HiddenInput())

    #amount.widget.attrs.update({'autofocus':'autofocus','autocomplete': 'off',  'class': 'input'})

    def __init__(self, *args, **kwargs):
        self.user_profile =  kwargs.pop('initial')
	self.balance = self.user_profile.balance
	self.deposits=self.user_profile.poems.all().count()
        super(WithdrawForm,self).__init__(*args, **kwargs)

    def clean(self):

        #withdraw_amount = self.cleaned_data['amount']
        withdraw_amount = 1 
        select_choice = self.cleaned_data['choice']
        print("Cleaning withdraw form, amount requested: {}".format(withdraw_amount))
        
        if self.user_profile is not None:
            print("User_profile passed from view is valid: {}".format(self.user_profile))
            print("Current Balance: {}".format(self.user_profile.balance))
            print("Current Personal Deposit Balance: {}".format(self.deposits))

            if int(withdraw_amount) == 0:
                raise forms.ValidationError("You're clever; printing 0 poems", code='invalid')

            if select_choice == 'r':
                if int(self.user_profile.balance) < int(withdraw_amount):
                    raise forms.ValidationError("Deposit more words", code='invalid')
            else:
                if self.deposits < int(withdraw_amount):
                    raise forms.ValidationError("Deposit more words", code='invalid')
        else:
            raise forms.ValidationError('User is no longer logged in', 
                                        code='invalid')

        #return {('amount', self.cleaned_data['amount']), ('choice', self.cleaned_data['choice'])}
        return {('amount', '1'), ('choice', self.cleaned_data['choice'])}


class D1Form(forms.Form):
    plural_noun = forms.CharField(label='Plural Noun')
    plural_nouns = {"d1": Word.objects.filter(category='pn').values_list('word', flat=True).order_by('?')[:9]}
    choices = plural_nouns

    def __init__(self, *args, **kwargs):
        print('kwargs: {}'.format(kwargs))
        self.plural_nouns = {"d1": Word.objects.filter(category='pn').values_list('word', flat=True).order_by('?')[:9]} 
        self.choices = self.plural_nouns
        super(D1Form, self).__init__(*args, **kwargs)


class D2Form(forms.Form):
    adjective = forms.CharField(label='Adjective')
    adjectives = {"d2": Word.objects.filter(category='a').values_list('word', flat=True).order_by('?')[:9]}
    choices = adjectives

    def __init__(self, *args, **kwargs):
        print('kwargs: {}'.format(kwargs))
    	self.adjectives = {"d2": Word.objects.filter(category='a').values_list('word', flat=True).order_by('?')[:9]}
	self.choices = self.adjectives
        super(D2Form, self).__init__(*args, **kwargs)


class D3Form(forms.Form):
    plural_noun2 = forms.CharField(label='Plural Noun')
    plural_nouns = {"d3": Word.objects.filter(category='pn').values_list('word', flat=True).order_by('?')[:9]}
    choices = plural_nouns
    
    def __init__(self, *args, **kwargs):
        print('kwargs: {}'.format(kwargs))
        self.plural_nouns = {"d3": Word.objects.filter(category='pn').values_list('word', flat=True).order_by('?')[:9]} 

        self.choices = self.plural_nouns
        super(D3Form, self).__init__(*args, **kwargs)

class D4Form(forms.Form):
    color = forms.CharField(label='Color')
    colors = {"d3": Word.objects.filter(category='c').values_list('word', flat=True).order_by('?')[:9]}
    choices = colors
    
    def __init__(self, *args, **kwargs):
        print('kwargs: {}'.format(kwargs))
        self.colors = {"d4": Word.objects.filter(category='c').values_list('word', flat=True).order_by('?')[:9]} 
        self.choices = self.colors
        super(D4Form, self).__init__(*args, **kwargs)

class D5Form(forms.Form):
    noun = forms.CharField(label='Noun')
    nouns = {"d5": Word.objects.filter(category='n').values_list('word', flat=True).order_by('?')[:9]}
    choices = nouns
    
    def __init__(self, *args, **kwargs):
        print('kwargs: {}'.format(kwargs))
        self.nouns = {"d5": Word.objects.filter(category='n').values_list('word', flat=True).order_by('?')[:9]} 
        self.choices = self.nouns
        super(D5Form, self).__init__(*args, **kwargs)

class D6Form(forms.Form):
    adjective2 = forms.CharField(label='Adjective')
    adjectives = {"d6": Word.objects.filter(category='a').values_list('word', flat=True).order_by('?')[:9]}
    choices = adjectives
    
    def __init__(self, *args, **kwargs):
        print('kwargs: {}'.format(kwargs))
        self.adjectives = {"d6": Word.objects.filter(category='a').values_list('word', flat=True).order_by('?')[:9]} 
        self.choices = self.adjectives
        super(D6Form, self).__init__(*args, **kwargs)


class D7Form(forms.Form):
    verb = forms.CharField(label='Verb')
    verbs = {"d6": Word.objects.filter(category='v').values_list('word', flat=True).order_by('?')[:9]}
    choices = verbs
    
    def __init__(self, *args, **kwargs):
        print('kwargs: {}'.format(kwargs))
        self.verbs = {"d7": Word.objects.filter(category='v').values_list('word', flat=True).order_by('?')[:9]} 
        self.choices = self.verbs
        super(D7Form, self).__init__(*args, **kwargs)
