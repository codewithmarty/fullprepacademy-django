from django.urls import path
from .views import *

urlpatterns = [
    path('', tutoring_index),
    path('about/', tutoring_about),
    path('contact/', tutoring_contact),
    path('services/', tutoring_services),
    path('booking/', book_now),
    path('signup/', signup, name='signup'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout')
]