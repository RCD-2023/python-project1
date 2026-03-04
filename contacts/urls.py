from django.urls import path
from . import views

# calea este /listings respectiv calea catre un id #/listings/23
urlpatterns = [
    path('contact',views.contact, name='contact' ),
    
]