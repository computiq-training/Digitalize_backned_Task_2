from django.contrib import admin
from django.urls import path
from django.urls import path
from ninja import NinjaAPI
from files_management.controller import prodect_controllar
api=NinjaAPI()
api.add_router('/prodects',prodect_controllar)
urlpatterns = [
    path('admin/', admin.site.urls),
      path('api/',api.urls),
]
