from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .models import planTable, itemTable, workoutTable
from .forms import planForm

# Create your views here.

def index(request):
    
    return render(request, 'workoutapp/index.html', {})

def home(request):
    
    return render(request, 'workoutapp/home.html', {})


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.success(request, ("There was an error logging in"))
            return redirect('login')
    else:
        
        return render(request, 'workoutapp/login.html', {})
    
def logout_user(request):
    logout(request)
    
    messages.success(request, ("You were logged out"))
    
    return redirect('index')

def register_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            form.save()
            
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            
            user = authenticate(username=username, password=password)
            login(request,user)
            
            messages.success(request,("Register SUcces"))
            
            return redirect('index')
        
    else:
        form = UserCreationForm()
    
    
    return render(request, 'workoutapp/register_user.html', {
        'form':form
    })
    
    
def createPlan(request):
    
    form = planForm
    
    if request.method == "POST":
        form = planForm(request.POST)
        
        if form.is_valid():
            
            plan = form.save(commit=False)
            plan.user = request.user
            plan.save()
            return redirect('index')
    
    
    context = {'form':form}
    return render(request, 'workoutapp/create_plan.html', context)

@login_required(login_url='/register_user/')
def myPlan(request):
        
    my_plan = planTable.objects.filter(user=request.user)
    print('user : ', request.user)
    #print('data : ', my_plan)
    context = {'my_plan':my_plan}
    return render(request, 'workoutapp/my_plan.html', context)
