from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI
from files_management.controller import post_controller



api = NinjaAPI()
api.add_router('/posts' , post_controller)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api.urls)
]