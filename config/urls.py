
from django.contrib import admin
from django.urls import path
from files_management.mycontroller import files_controller
from ninja import NinjaAPI

api = NinjaAPI()
api.add_router('/', files_controller)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api.urls),
]
