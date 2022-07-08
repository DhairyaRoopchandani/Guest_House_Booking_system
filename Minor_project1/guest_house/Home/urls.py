from django.urls import path
from . import views

urlpatterns = [
   path('',views.Home,name="Home"),
   path('login/',views.login,name="login"),
   path('signup/',views.signup,name="signup"),
   path('logout/',views.logout,name="logout"),
   path('dashboard/',views.dashboard,name="dashboard"),
   path('profile/',views.profile,name="profile"),
   path('history/',views.booking_history,name="booking_history")
]