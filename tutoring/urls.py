from django.urls import path
from .views import *

urlpatterns = [
    path('', tutoring_index),
    path('about/', tutoring_about),
    path('contact/', tutoring_contact, name='contact'),
    path('tutoring/', tutoring_services, name='tutoring_services'),
    path('tutoring/<str:subject>/', subject_detail, name='subject_detail'),
    path('materials/', materials, name='materials'),
    path('booking/', book_now),
    path('contact_submit/', contact_form_submission, name='contact_submit'),
    path('thankyou/', email_confirmation, name='email_confirmation'),
    path('signup/', signup, name='signup'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout')
]