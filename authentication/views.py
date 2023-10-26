from django.shortcuts import render
from . forms import LoginForm
from django.contrib.auth import authenticate ,login ,logout
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
# Create your views here.


# user login view
@csrf_exempt
def user_login(request):
    if request.method == 'POST':
       
        uname = request.POST.get('username')
        lower_convert = uname.lower()
        upass = request.POST.get('password')

        user = authenticate(username = lower_convert, password = upass)
        if user is not None:
            login(request,user)
            return HttpResponseRedirect('/')
        else:
            messages.warning(request,'User not found')
            return HttpResponseRedirect('/')
    else:
        context = {'form':LoginForm()}
        return render (request,'authentication/login.html',context)


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')