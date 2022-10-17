from django.shortcuts import render
# Create your views here.
from ninja import Router

post_controller = Router()

@post_controller.get('/')
def list_post(request):
    return{'Message:goooo'}