
from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI
from files_management.controller import post_controller

api=NinjaAPI()
urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/' , post_controller)
    
]
