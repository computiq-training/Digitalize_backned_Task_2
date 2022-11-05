from django.shortcuts import render
from ninja import Router 
import re
from files_management.utils import list_posts,save_post,get_post,del_post

post_controller = Router()
@post_controller.get('')
def list_posts(request):
  return list_posts()


@post_controller.get('/{title}')
def get_post(request ,title):
  return get_post(title)

@post_controller.post('')
def save_post(request , title , content):
  return save_post(title,content)



@post_controller.delete('/{title}')
def del_post(request ,title):
  return del_post(title)

