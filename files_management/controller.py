from gc import get_objects
from turtle import title
from django.shortcuts import render
# Create your views here.
from ninja import Router,Schema
from files_management.utils import list_posts,save_post,get_post,del_post

class BodyIn(Schema):
    title :str
    content:str

Posts_Conrtoller=Router()


# to list all posts
@Posts_Conrtoller.get('get')
def list_all_posts(request):
    return list_posts()


# to retrieve a certain post

@Posts_Conrtoller.get('/{title}')
def retrieve_post(request ,title):
    return get_post(title)




# to create a new post
@Posts_Conrtoller.post('')
def create_post(request,title,content):
    return save_post(title,content)



# to update a certain post
# @Posts_Conrtoller.put('')
# def update_post(request,payload:BodyIn()):
#     pass
    # payload.title=title
    # payload.content=content

    # filename = f"posts/{title}.md"
    # if default_storage.exists(filename):
    #     default_storage.add(filename,ContentFile(content))
    # default_storage.save(filename, ContentFile(content))
    # return{'Message':f'Post {title} Created Successfully'}



# to delete a certain post
@Posts_Conrtoller.delete('')
def delet_post(request,title):
    return del_post(title)
