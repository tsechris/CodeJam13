from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.index),
    path("camera/", views.camera),
    path("", views.signin),
    path("api/", views.api),

]