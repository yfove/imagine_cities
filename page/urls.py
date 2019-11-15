from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('ourwork/', views.our_work, name='ourwork'),
    path('getinvolved/', views.get_involved, name='getinvolved'),
    path('contactus/', views.contact_us, name='contactus'),
    path('ourteam/', views.our_team, name='ourteam'),
]
