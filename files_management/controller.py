import re
from django.shortcuts import render
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from ninja import Router 

post_controller = Router()

# function to get all the posts
@post_controller.get('')
def list_posts(request):
    _, filenames = default_storage.listdir("posts")
    return list(sorted(re.sub(r"\.md$", "", filename)
                       for filename in filenames if filename.endswith(".md")))

# function to create new post and save it 
@post_controller.post('')
def save_post(request , title , content):
    filename = f"posts/{title}.md"
    if default_storage.exists(filename):
        default_storage.delete(filename)
    default_storage.save(filename, ContentFile(content))

# function to get the post using the title 
@post_controller.get('/{title}')
def get_post(request ,title):
    try:
        f = default_storage.open(f"posts/{title}.md")
        return f.read().decode("utf-8")
    except FileNotFoundError:
        return None
#function to delete a post using title
@post_controller.delete('/{title}')
def del_post(request ,title):
    filename = f"posts/{title}.md"
    default_storage.delete(filename)
    return {'messege': 'deleted.'}
   