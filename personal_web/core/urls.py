from django.urls import path
from . import views
urlpatterns = [
    path( '', views.home.as_view() ,name='home'),
    path( 'about-me/', views.about.as_view() ,name='about'),
    path( 'contact-me/', views.contact.as_view() ,name='contact'),
]
