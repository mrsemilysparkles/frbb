from datetime import datetime
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.contrib import messages 
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from formtools.wizard.views import SessionWizardView

from .forms import CreateAccountForm, CreatePinForm, D1Form, D2Form, D3Form,\
        WithdrawForm, D4Form, D5Form, D6Form, D7Form, AForm, BForm

from .models import UserProfile, Poem, Word

from .printer import  print_new_account_info, print_poem
#from .lights import new_account_lighting, deposit_lighting, withdraw_lighting, logout_lighting, out_of_paper_lighting, login_lighting
#from .sounds import new_account_sound, deposit_sound, withdraw_sound, logout_sound, login_sound

LOGIN_FORMS = [("account", AForm),
               ("pin", BForm)]

LOGIN_TEMPLATES = {"account": "frbb/account.html",
                   "pin": "frbb/pin.html"}

REGISTER_FORMS = [("create-account", CreateAccountForm),
                 ("create-pin", CreatePinForm)]

REGISTER_TEMPLATES = {"create-account": "frbb/create-account.html",
                      "create-pin": "frbb/create-pin.html"}

DEPOSIT_FORMS = [("D1", D1Form),
                 ("D2", D2Form),
                 ("D3", D3Form),
                 ("D4", D4Form),
                 ("D5", D5Form),
                 ("D6", D6Form),
                 ("D7", D7Form),
                ]

DEPOSIT_TEMPLATES = {"D1": "frbb/d1deposit.html",
                     "D2": "frbb/d2deposit.html",
                     "D3": "frbb/d3deposit.html",
                     "D4": "frbb/d4deposit.html",
                     "D5": "frbb/d5deposit.html",
                     "D6": "frbb/d6deposit.html",
                     "D7": "frbb/d7deposit.html"}

def hash(id, type):
   number = (7 * int(id)) + 997
   return str(type) + str(number)

WITHDRAW_FORMS = [("withdraw", WithdrawForm)]
WITHDRAW_TEMPLATES = {"withdraw": "frbb/withdraw.html"}

def index(request):
    if request.user.is_authenticated(): 
        return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)
    context_dict = {'boldmessage': "I am bold font from the context"}
    return render(request, 'frbb/index.html', context_dict)

class RegisterWizard(SessionWizardView):

    def done(self, form_list, form_dict, **kwargs):
        cd = self.get_all_cleaned_data()
        user = User()
        user_profile = UserProfile()
        user.username = cd['account_number']
        user.set_password(cd['pin_number'])
        user.save()
        user_profile.user = user
        user_profile.save()
        
        authenticated_user = authenticate(username=cd['account_number'],
                                          password=cd['pin_number'])
        if authenticated_user is not None:
            login(self.request, authenticated_user)
            terms_of_service = "These are some terrible TOS conditions"
            #new_account_sound()
            #new_account_lighting()
            print_new_account_info(account_number=cd['account_number'],
                                       pin_number=cd['pin_number'],
                                       tos=terms_of_service);


            return HttpResponseRedirect('/frbb/dashboard')
        else:
            return HttpResponseRedirect('/frbb')

    def get_template_names(self):
        return [REGISTER_TEMPLATES[self.steps.current]]


@method_decorator(login_required, name='dispatch')
class DepositWizard(SessionWizardView):
    def done(self, form_list, form_dict, **kwargs):
        cd = self.get_all_cleaned_data()
        cd['plural_noun'] = cd['plural_noun'].capitalize()
        cd['noun'] = cd['noun'].capitalize()
        poem = '%(plural_noun)s are %(adjective)s; %(plural_noun2)s are of a %(color)s hue. %(noun)s is %(adjective2)s. May I %(verb)s you?' %cd
        p = Poem.objects.create(text=poem, category='c')
        p.withdrawn= False
        p.save()
        up = UserProfile.objects.get(user__username=self.request.user.username)
        up.poems.add(p)
        up.balance +=1
        up.save()
        
        #deposit_sound()
        #deposit_lighting()

        poem = str(p.text)
        print("Deposited Poem: {}".format(poem))
	upc_code = str(datetime.now().strftime('%M%d%H')) + str(hash(self.request.user.username, 'c'))
	print("UPC_CODE: {}".format(upc_code))
        print_poem(poem, upc_code)

        return render(self.request, 'frbb/deposit.html', {'poem': poem})

    def get_template_names(self):
        return [DEPOSIT_TEMPLATES[self.steps.current]]
         

@login_required
def user_logout(request):
    resp = logout(request)
    return render(request, 'frbb/index.html', {})


class LoginWizard(SessionWizardView):
    def get_template_names(self):
        return [LOGIN_TEMPLATES[self.steps.current]]
    
    def done(self, form_list, form_dict, **kwargs):
        cd = self.get_all_cleaned_data()

        user = authenticate(username = cd['username'],
                            password = cd['password'])

        if user is not None:
            login(self.request, user)
            #login_sound()
            #login_lighting()
            return HttpResponseRedirect('/frbb/dashboard')
        else:
            messages.add_message(self.request, messages.ERROR, 'Authentication Failure')
            return HttpResponseRedirect('/frbb/invalid')

        return HttpResponseRedirect('frbb/')


@method_decorator(login_required, name='dispatch')
class WithdrawWizard(SessionWizardView):
   
    def get_form_initial(self, step, **kwargs):
        up = UserProfile.objects.get(user__username=self.request.user.username)
        return up

    def done(self, form_list, form_dict, **kwargs):
        up = UserProfile.objects.get(user__username=self.request.user.username)
        cd = self.get_all_cleaned_data()
        withdraw_amount = int(cd['amount'])
        print('Withdraw request data: {}'.format(cd))
    
        if cd['choice'] == 'r':
	    up.balance -= withdraw_amount 
            poems = Poem.objects.all().order_by('?')[:withdraw_amount]
        else:
	    poems = up.poems.all().order_by('?')[:withdraw_amount]

        up.withdrawn += 1;
        up.save()
	
        #withdraw_sound()
        #withdraw_lighting()
        
	upc_code = str(datetime.now().strftime('%M%d%H')) + str(hash(self.request.user.username, cd['choice']))
	for poem in poems:
            print_poem(str(poem.text), upc_code)


	return HttpResponseRedirect('/frbb/logout') 

    def get_template_names(self):
        return [WITHDRAW_TEMPLATES[self.steps.current]]


@login_required
def dashboard(request):
    up = UserProfile.objects.get(user__username=request.user.username)
    up.login_count += 1
    up.save()
    print up
    context_dict = {'balance': up.balance, 'user': request.user.username, 'deposits': up.poems.all().count()}
    return render(request, 'frbb/dashboard.html',context_dict)


def invalid(request):
    return HttpResponseRedirect('/frbb/login')

