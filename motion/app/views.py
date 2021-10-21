from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from app.forms import UserRegistrationForm, UserLoginFrom, ProofForm
from django.contrib.auth.decorators import login_required
from app.models import *
#flash message
from django.contrib import messages
# Create your views here.

def index(request):
    setting = Setting.objects.all().order_by('-id')[0]
    context = {
         'setting': setting
     }
    return render(request, 'app/index.html', context)

def registerPage(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    else:
        context = {}
        if request.POST:
            form = UserRegistrationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('login')
            context['form'] = form  
        else:
            form = UserRegistrationForm()
            context['form'] = form  
        return render(request, 'app/signup.html', context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    else:
        context = {}
        if request.POST:
            form = UserLoginFrom(request.POST)
            if form.is_valid():
                email = request.POST['email']
                password = request.POST['password']
                user = authenticate(request, email=email, password=password)
                if user is not None:
                    login(request, user)
                    return redirect("dashboard")
            else:
                context['form'] = form
        else:
            form = UserLoginFrom()
            context['form'] = form
        return render(request, 'app/login.html', context)

def logoutPage(request):
    logout(request)
    return redirect("login")

@login_required(login_url='login')
def dashboardPage(request):
    error = Error.objects.all().order_by('-id')[0]
    packages = Package.objects.all().order_by('-id')
    settings = Setting.objects.all().order_by('-id')[0]
    approved = Approved.objects.all()
    approved_count = Approved.objects.filter(user_name=request.user).count()
    interest = Interest.objects.all()
    divinde = Dividens.objects.all()
    ref = Referral_reward.objects.all()
    context = {
        'packages' : packages,
        'setting' : settings,
        'proof': ProofForm,
        'data' : error,
        'approved': approved,
        'ccount': approved_count,
        'interest' : interest,
        'divinde' : divinde,
        'ref' : ref,
    }
    if request.method == 'POST':
        form = ProofForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, f'Proof sent admin will get back to you!')
        else:
            proof = ProofForm()
    return render(request, 'app/investment.html', context)