from django.shortcuts import render, redirect

def tutoring_index(request):
    return render(request, 'tutoring/landing.html')

def tutoring_about(request):
    return render(request, 'tutoring/about.html')

def tutoring_contact(request):
    return render(request, 'tutoring/contact.html')

def tutoring_services(request):
    return render(request, 'tutoring/services.html')