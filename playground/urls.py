from django.urls import path
from . import views

# URL configuration
# always end the routes wiht /
urlpatterns=[
    path('hello/', views.say_hello)
]