from django.contrib import admin
from django.urls import path
from blog import views as blog_views

app_name = "blog"

urlpatterns = [
    
    path('', blog_views.blog, name= "home"),
    path("example/", blog_views.example, name= "example"),
    
]
