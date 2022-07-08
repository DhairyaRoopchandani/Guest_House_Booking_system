from django.urls import path
from . import views

urlpatterns = [
   path('',views.booking,name="booking"),
   path(r'search/', views.find_hotel, name='search'),
   path(r'summary/', views.summary, name='summary'),
   path(r'cancel/', views.cancel_booking, name='cancel_booking')
]