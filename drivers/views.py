from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.
@login_required(login_url='/accounts/login/')
def d_index(request):
    return render(request, 'd-index.html')

@login_required(login_url='/accounts/register/')
def d_homepage(request):
    return render(request, 'd-homepage.html')

def logout(request):
    return render(request, 'd-index.html')
