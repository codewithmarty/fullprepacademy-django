from django.urls import path
from .views import *

urlpatterns = [
    path('', tutoring_index),
    path('about/', tutoring_about),
    path('contact/', tutoring_contact),
    path('services/', tutoring_services)
]