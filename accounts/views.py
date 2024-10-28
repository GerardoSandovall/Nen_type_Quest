from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required

#Main menu
def Main(request):
    return render(request, 'Main.html', {})

#Registro
def Register(request):

    if request.method == ('GET'):
        return render(request, 'Register.html', 
                  {'form': UserCreationForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username= request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('Main')
            except IntegrityError:
                Error= 'User alredy exist'
            return render(request, 'Register.html', 
                  {'form': UserCreationForm, 'Error':Error})
        else:
            Error= 'password does not match'
            return render(request, 'Register.html', 
                  {'form': UserCreationForm, 'Error':Error})
        
#Inicio de sesion
def Login(request):
    if request.method == ('GET'):
         return render(request, 'Login.html', 
                  {'form': AuthenticationForm})
    else:
        try:
            user= authenticate(request, username= request.POST['username'], password = request.POST['password'])
            login(request, user)
            return redirect('Main')
        except AttributeError:
            Error="Password is incorrect"
            return render(request, 'Login.html', 
                  {'form': AuthenticationForm, 'Error': Error})
 
#Cerrar sesion
@login_required
def Logout(request):
    try:
        logout(request)
        return redirect('Main')
    except:
        pass