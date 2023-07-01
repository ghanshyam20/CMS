from django.urls import path
from . import views

app_name = 'hotel_app'  # Optional: specify the app name

urlpatterns = [
    path("", views.home, name="home"),
    path("contact/",views.contact,name="contact"),
    path("features/",views.features,name="features"),
    # Add more URL patterns for the hotel_app here
    # Example: path("rooms/", views.room_list, name="room_list"),
]
