from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('about', views.about, name="about"),
    path('class', views._, name="class"),
    path('contact', views.contact, name="contact"),
    path('message', views.message, name="message"),
    # path('class/detail', views.single, name="single"),
]