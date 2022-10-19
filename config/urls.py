
from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI
from files_management.controller import Posts_Conrtoller
from files_management.utils import list_posts
# from files_management.utils import utils  

#from account.views import products_controller,users

api=NinjaAPI()

api.add_router('/Posts',Posts_Conrtoller)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',api.urls),
]
