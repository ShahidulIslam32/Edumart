from django.contrib.auth.signals import user_logged_in
from django.shortcuts import render
from login_test_app.forms import UserForm, UserInfoForm
from django.core.mail import send_mail
#from django.conf import settings


#login module omport from django

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth.models import User 
from login_test_app.models import UserInfo

# Create your views here.


def index(request):

    diction = {'title':'Edumark'}
    return render(request, 'file/index.html',context=diction)


def register(request):
    registered  = False
    
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        user_info_form = UserInfoForm(data=request.POST)

        if user_form.is_valid() and user_info_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            user_info = user_info_form.save(commit=False)
            user_info.user = user

            if 'profile_pic' in request.FILES:
                user_info.profile_pic = request.FILES['profile_pic']
                
            user_info.save()
            registered = True
    else:    
        user_form = UserForm()
        user_info_form = UserInfoForm()
    diction = {'user_form': user_form,'user_info_form': user_info_form, 'registered': registered,'title':'User Registration'}
    return render(request, 'file/signup.html', context=diction)

#login function 

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
       

        if user:
           if  user.is_active:
               login(request, user)
               print('Login Successfull !!')
               return HttpResponseRedirect(reverse('login_test_app:dashboard'))
           else:
               return  HttpResponse('Your Account is Not Active !! Try Again')

        else:
                return render(request,'file/warn.html')
    else:
        return render(request,'file/login.html', context={})
     
    
# others function
def contact_us(request):
    diction = {'title': 'Contact Us'}
    return render(request, 'file/contact.html', context=diction)


def about_us(request):
    diction = {'title':'About Us'}
    return render(request, 'file/about.html', context=diction)

def dashboard(request):
    diction = {'title':'User Dashboard'}
    return render(request, 'file/dashboard.html', context=diction)


def warn(request):
    return render(request, 'file/warn.html',)

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('login_test_app:index'))

def profile(request):
    diction = {}
    if request.user.is_authenticated:
        current_user = request.user
        user_id = current_user.id
        user_basic_info = User.objects.get(pk=user_id)
        user_more_info = UserInfo.objects.get(user__pk=user_id)
        
        
        diction = {'user_basic_info':user_basic_info ,'user_more_info':user_more_info}
    return render(request, 'file/profile.html', context=diction)


