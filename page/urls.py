from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='page-home'),
    path('about/', views.about, name='page-about'),
    path('ourwork/', views.our_work, name='page-ourwork'),
    path('getinvolved/', views.get_involved, name='page-getinvolved'),
    path('contactus/', views.contact_us, name='contact-us'),
]
