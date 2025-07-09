from django .shortcuts import render, redirect
from django.contrib.auth.models import User
from todo import models
from todo.models import TODO
# Create your views here.

def singup(request):
    if request.method=='POST':
        fnm=request.POST.get('fnm')
        emailid = request.POST.get('emailid')
        pwd= request.POST.get('pwd')
        print(fnm, emailid, pwd)
        my_user = User.objects.create_user(username=fnm, email=emailid, password=pwd)
        my_user.save()
        return redirect("login")
    return render(request, 'singup.html')




    return render (request, 'singup.html')