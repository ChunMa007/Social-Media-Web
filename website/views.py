from django.shortcuts import render, redirect
from .forms import UserLoginForm, UserSignUpForm, UserProfileForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def user_login(request):
    form = UserLoginForm(request.POST or None)
    
    if request.method == "POST" and form.is_valid():
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        
        user = authenticate(request, username=email, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, "Login successfully")
            return redirect('post:home')
        else:
            messages.error(request, "Invalid Account")
    
    return render(request, 'login.html', {
        'form': form,
    })

def user_signup(request):
    if request.method == "POST":
        user_form = UserSignUpForm(request.POST or None)
        profile_form = UserProfileForm(request.POST or None, request.FILES or None)
        
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            
            user_profile = profile_form.save(commit=False)
            user_profile.user = user
            user_profile.save()
            
            messages.success(request, "Signup Successfully")
            return redirect('website:login')
        else:
            messages.error(request, "Invalid Input, Try Again!")
        
    else:
        user_form = UserSignUpForm()
        profile_form = UserProfileForm()
    
    
    return render(request, 'signup.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })