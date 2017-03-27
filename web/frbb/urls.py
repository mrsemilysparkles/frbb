from django.conf.urls import url, include
from frbb import views
from frbb import forms

urlpatterns = [ 
        url(r'^$',views.index, name='index'),
        url(r'^dashboard/$',views.dashboard, name='dashboard'),        
        url(r'^login/$',views.LoginWizard.as_view(views.LOGIN_FORMS), name='login'),
        url(r'^register/$',views.RegisterWizard.as_view(views.REGISTER_FORMS), 
                                                       name='register'),
        url(r'^logout/',views.user_logout, name='logout'),
        url(r'^deposit/',views.DepositWizard.as_view(views.DEPOSIT_FORMS), name='deposit'),
        url(r'^withdraw/',views.WithdrawWizard.as_view(views.WITHDRAW_FORMS), name='withdraw'),
#        url(r'^print/',views.u_print, name='print'),
        url(r'^invalid/', views.invalid, name='invalid'),] 
