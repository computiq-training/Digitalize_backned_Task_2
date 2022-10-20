from django.shortcuts import render
from ninja import Router
# Create your views here.
from files_management.utils import list_posts, get_post, save_post, del_post

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
def create_new_post(request, tiltle, content):
    return save_post(tiltle, content)

# to update a certain post
@postController.put('')
def update_certain_post(request, title):
    return save_post(title)

#delete post
@postController.delete('')
def delete_post(request, title, content):
    return del_post(title, content)