from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='waitlist'),
    path('inlist', views.inlist, name='inlist'),
]