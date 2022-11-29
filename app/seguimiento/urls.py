from django.urls import path
from app.seguimiento import views

urlpatterns = [
    path('', views.dashboard)
]
