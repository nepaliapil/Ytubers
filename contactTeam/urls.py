from django.urls import path
from . import views

urlpatterns = [
    path('contactTeam', views.contactTeam, name="contactTeam"),
]


