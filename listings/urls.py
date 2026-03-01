from django.urls import path
from . import views

# calea este /listings respectiv calea catre un id #/listings/23
urlpatterns = [
    path('',views.index, name='listings' ),
    path('<int:listing_id>',views.listing, name='listing' ),
    path('search', views.search, name='search' ),
]