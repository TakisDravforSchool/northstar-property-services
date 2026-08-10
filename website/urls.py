from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('services/', views.services, name='services'),
    path('about/', views.about, name='about'),
    path('gallery/', views.gallery, name='gallery'),
    path('contact/', views.contact, name='contact'),
    path('residential-pricing/', views.residential_pricing, name='residential_pricing'),
    path('commercial-pricing/', views.commercial_pricing, name='commercial_pricing'),
]