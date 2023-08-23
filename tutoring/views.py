from django import forms
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.core.mail import send_mail
import bleach
import environ
env = environ.Env()
environ.Env.read_env()
from .courses import courses

class MyForm(forms.Form):
    name = forms.CharField(max_length=255)
    email = forms.CharField(max_length=255)
    message = forms.CharField(widget=forms.Textarea)

def contact_form_submission(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            sanitized_name = bleach.clean(form.cleaned_data['name'])
            sanitized_email = bleach.clean(form.cleaned_data['email'])
            sanitized_message = bleach.clean(form.cleaned_data['message'])
            send_mail(
                f'New Inquiry for Full Prep Academy from {sanitized_name}',
                f'Name: {sanitized_name}\nSender: {sanitized_email}\n{sanitized_message}',
                env('EMAIL_HOST_USER'), 
                [env('EMAIL_HOST_USER')],
                fail_silently=False,
            )
            return redirect('/thankyou')
    else:
        return redirect('/contact')

def email_confirmation(request):
    return render(request, 'tutoring/thankyou.html')
    
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
            return redirect('/')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('/')

def materials(request):
    return render(request, 'tutoring/materials.html', { 'user': request.user })

def book_now(request):
    return render(request,  'tutoring/book_now.html', { 'user': request.user })

def tutoring_index(request):
    return render(request, 'tutoring/landing.html', { 'user': request.user })

def subject_detail(request, subject):
    return render(request, 'tutoring/subject_detail.html', { 'course': courses[subject] })

def tutoring_about(request):
    return render(request, 'tutoring/about.html', { 'user': request.user })

def tutoring_contact(request):
    return render(request, 'tutoring/contact.html', { 'user': request.user })

def tutoring_services(request):
    return render(request, 'tutoring/tutoring.html', { 'user': request.user })