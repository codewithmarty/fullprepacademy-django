from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')  # Redirect to the login page
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')  # Redirect to the home page
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('/')

def tutoring_index(request):
    return render(request, 'tutoring/landing.html', { 'user': request.user })

def tutoring_about(request):
    return render(request, 'tutoring/about.html', { 'user': request.user })

def tutoring_contact(request):
    return render(request, 'tutoring/contact.html', { 'user': request.user })

def tutoring_services(request):
    return render(request, 'tutoring/services.html', { 'user': request.user })