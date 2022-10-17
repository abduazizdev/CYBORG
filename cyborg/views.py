from email import header
from multiprocessing import context
from django.shortcuts import render
from .forms import *
from .models import *
from django.shortcuts import redirect

def home(request):
    return render(request, 'pages/home.html')

def index(request):
    
    header = Header.objects.all()
    
    context = {
       'header': header
    }
    
    return render(request, 'includes/index.html', context)

def browse(request):
    return render(request, 'includes/browse.html')


def details(request):
    return render(request, 'includes/details.html')
    


def streams(request):
    return render(request, 'includes/streams.html')



def profile(request):
    return render(request, 'includes/profile.html')


def signup(request):
    form = Registration()
    if request.method == "POST":
        form = Registration(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    return render(request, 'registration/signup.html', {"form": form})



def logout(request):
    return render(request, 'registration/logout.html')


def logout_confirmation(request):
    return render(request, 'registration/logout-confirmation.html')