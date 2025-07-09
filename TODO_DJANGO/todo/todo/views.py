from django .shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from todo import models
from todo.models import TODO
# Create your views here.

def singup(request):
    if request.method=='POST':
        fnm=request.POST.get('fnm')
        emailid = request.POST.get('emailid')
        pwd= request.POST.get('pwd')
        print(fnm, emailid, pwd)
        
        # Check if username already exists
        if User.objects.filter(username=fnm).exists():
            messages.error(request, 'Username already exists. Please choose a different username.')
            return render(request, 'singup.html')
        
        # Check if email already exists
        if User.objects.filter(email=emailid).exists():
            messages.error(request, 'Email already registered. Please use a different email.')
            return render(request, 'singup.html')
        
        try:
            my_user = User.objects.create_user(username=fnm, email=emailid, password=pwd)
            my_user.save()
            messages.success(request, 'Account created successfully! Please login.')
            return redirect("login")
        except Exception as e:
            messages.error(request, f'Error creating account: {str(e)}')
            return render(request, 'singup.html')
    
    return render(request, 'singup.html')

def loginn(request):
    if request.method == 'POST':
        fnm = request.POST.get('fnm')
        pwd = request.POST.get('pwd')
        
        user = authenticate(request, username=fnm, password=pwd)
        if user is not None:
            login(request, user)
            return redirect('todo')
        else:
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'login.html')

@login_required
def todo(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            TODO.objects.create(user=request.user, title=title, status=False)
        return redirect('todo')
    
    todos = TODO.objects.filter(user=request.user)
    return render(request, 'todo.html', {'res': todos, 'user': request.user.username})

@login_required
def edit_todo(request, srno):
    todo = TODO.objects.get(srno=srno, user=request.user)
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            todo.title = title
            todo.save()
        return redirect('todo')
    
    return render(request, 'edit_todo.html', {'todo': todo})

@login_required
def delete_todo(request, srno):
    todo = TODO.objects.get(srno=srno, user=request.user)
    todo.delete()
    return redirect('todo')

@login_required
def toggle_todo(request, srno):
    todo = TODO.objects.get(srno=srno, user=request.user)
    todo.status = not todo.status
    todo.save()
    return redirect('todo')

def signout(request):
    logout(request)
    return redirect('login')