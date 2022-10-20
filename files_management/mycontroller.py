from files_management.utils import list_posts, get_post, save_post, del_post, exist_post

from ninja import Router, Schema



class FileBody(Schema):
    
    file_title: str
    file_content: str = None


class FileBodyUpdate(Schema):
 
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



@files_controller.put('/posts/{paraTitle}')
def update_file(request, payload: FileBodyUpdate, paraTitle):
    try:
        if exist_post(paraTitle):
            if paraTitle is not None and payload.file_content is not None:
                save_post(title=paraTitle, content=payload.file_content)
                return {'Message': 'File Updated Successfully'}
            else:
                return {'Message': 'Please provide file name and file content to update'}
        else:
            return {'Message': 'There is no file with that name'}
    except:
        return {'Message': 'There is an error occurs'}


@files_controller.delete('/posts/{paraTitle}')
def delete_file(request, paraTitle):
    try:
        if paraTitle is not None:
            if del_post(paraTitle):
                return {'Message': 'File deleted Successfully'}
            else:
                return {'Message': 'There is no file with that name, Please provide a correct file name to delete it'}
    except:
        return {'Message': 'There is an error occurs'}
