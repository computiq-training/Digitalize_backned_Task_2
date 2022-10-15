from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI
from files_management.FileManController import files_controller

api = NinjaAPI()

api.add_router('/', files_controller)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api.urls)
]
