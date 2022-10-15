from files_management.utils import list_posts, get_post, save_post, del_post
# from django.shortcuts import render
from ninja import Router, Schema


# Create your views here.

class FileBody(Schema):
    """this Schema for posting new post"""
    file_title: str
    file_content: str = None


class FileBodyUpdate(Schema):
    """this Schema for update post"""
    file_content: str = None


files_controller = Router()


# list all Posts
@files_controller.get('/posts')
def get_files(request):
    return list_posts()


@files_controller.get('/posts/{paraTitle}')
def get_files_by_title(request, paraTitle: str):
    try:
        if get_post(title=paraTitle):
            return get_post(title=paraTitle)
        elif get_post(title=paraTitle) is None:
            return {'Message': 'There is no post with that name'}
    except:
        return {'Message': 'There is an error occurs'}

# this method for posting new file
@files_controller.post('/posts')
def post_file(request, payload: FileBody):
    try:
        if payload.file_title is not None:
            save_post(title=payload.file_title, content=payload.file_content)
            return {'Message': 'File Saved Successfully'}
        else:
            return {'Message': 'Please provide file name'}
    except:
        return {'Message': 'There is an error occurs'}


# this method for updating existing file
@files_controller.put('/posts/{paraTitle}')
def update_file(request, payload: FileBodyUpdate, paraTitle):
    try:
        if paraTitle is not None and payload.file_content is not None:
            save_post(title=paraTitle, content=payload.file_content)
            return {'Message': 'File Updated Successfully'}
        else:
            return {'Message': 'Please provide file name and file content to update'}
    except:
        return {'Message': 'There is an error occurs'}


@files_controller.delete('/posts{paraTitle}')
def delete_file(request, paraTitle):
    try:
        if paraTitle is not None:
            del_post(paraTitle)
            return {'Message': 'File deleted Successfully'}
        else:
            return {'Message': 'Please provide file name and file content to delete'}
    except:
        return {'Message': 'There is an error occurs'}