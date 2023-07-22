from django.urls import path
from . import views
urlpatterns = [
    path( '', views.home.as_view() ,name='home'),
    path( 'contact-me/', views.contact.as_view() ,name='contact'),
    path( 'serveces/', views.services.as_view() ,name='services'),
]
