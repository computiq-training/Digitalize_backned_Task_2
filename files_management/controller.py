from django.shortcuts import render
from ninja import Router, Schema
# Create your views here.
from files_management.utils import list_posts, get_post, save_post, del_post

class BoydyIn(Schema):
    title: str
    content: str

postController = Router()

# to list all posts
@postController.get('')
def list_all_posts(request):
    return list_posts()

# to retrieve a certain post
@postController.get('posts/{title}')
def get_post_title(request, title):
    return get_post(title)

# to create a new post
@postController.post('')
def create_new_post(request, payload: BoydyIn):
    return save_post(payload.title, payload.content)

# to update a certain post
@postController.put('')
def update_certain_post(request, payload: BoydyIn):
    return save_post(payload.title)

#delete post
@postController.delete('')
def delete_post(request,payload: BoydyIn):
    return del_post(payload.title, payload.content)