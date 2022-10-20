from tkinter import N
from django.shortcuts import render
from ninja import Router,Schema # call Router and schema class from ninja package
from files_management.utils import list_posts,get_post,save_post,del_post # call utils functions

class BodyIn(Schema):
    post_name: str = None
    post_content: str


# Create your views here.
posts_cont=Router()

# Get All
@posts_cont.get('')
def posts_get_all(request):
    return {'All Posts':list_posts()}

# Get sertain file
@posts_cont.get('/{title}')
def posts_get_one(request,title):
    F_content=get_post(title=title)
    if F_content==None: return {'massege': 'Sorry, No post with this name!'}
    else: return {'File': F_content}

# Post new file
@posts_cont.post('')
def posts_post_new(request, payload: BodyIn):
    save_post(title=payload.post_name,content=payload.post_content)
    return {'massege': 'Post Saved successfully'}

# Update file
@posts_cont.put('/{title}')
def posts_update(request, title,payload: BodyIn):
    if title in list_posts():
        save_post(title=title,content=payload.post_content)
        return {'massege': 'Post updated successfully'}
    else: return {'massege': 'Sorry, No post with this name!'}

# Delete post
@posts_cont.delete('/{title}')
def post_delet(request,title):
    if title in list_posts():
        del_post(title)
        return {'massege': 'Post deleteted successfully'}
    else: return {'massege': 'Sorry, No post with this name!'}
    