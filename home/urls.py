from django.urls import path

from . import views

urlpatterns = [
    path("/home", views.index, name="home"),
    path("home/templates/home/signup.html", views.signup, name = "signup"),
    path("home/templates/home/home/templates/home/register.html", views.register, name = "register"),
    path('register',views.register , name = "register" )


]

