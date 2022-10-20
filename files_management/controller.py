from django.shortcuts import render
from ninja import Router, Schema
import re
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage


class TandC(Schema):
    title: str
    content: str = None


# Create your views here.

post_control = Router()


@post_control.get('')
def list_posts(request):
    """
    Returns a list of all names of blog posts.
    """
    _, filenames = default_storage.listdir("posts")
    return list(sorted(re.sub(r"\.md$", "", filename)
                       for filename in filenames if filename.endswith(".md")))


@post_control.get('/{title}')
def get_post(request, title):
    """
    Retrieves a post by its title. If no such
    post exists, the function returns None.
    """
    try:
        f = default_storage.open(f"posts/{title}.md")
        return f.read().decode("utf-8")
    except FileNotFoundError:
        return None


@post_control.put('')
def save_post(request, paylod: TandC):
    """
    Saves a blog post, given its title and Markdown
    content. If an existing post with the same title already exists,
    it is replaced.
    """
    filename = f"posts/{paylod.title}.md"
    if default_storage.exists(filename):
        default_storage.delete(filename)
    default_storage.save(filename, ContentFile(paylod.content))


@post_control.delete('/{title}')
def del_post(request, title):
    filename = f"posts/{title}.md"
    if default_storage.exists(filename):
        default_storage.delete(filename)
