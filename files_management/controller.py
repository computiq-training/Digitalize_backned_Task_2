from django.shortcuts import render
from ninja import Router,Schema
class BodyIn(Schema):
    name:str
    index:int
# Create your views here.
prodect_controllar=Router()
post=[

]


@prodect_controllar.get('')
def all_post(request):
    return post


@prodect_controllar.get('/{title}')
def get_post(request,title):
    return{'massge':'you are seccessfull to get title'}

@prodect_controllar.post('')
def creat(request,payload:BodyIn):
 post.append(payload.name)
 post.append(payload.index)
 return{'massge':'your  add is seccessfull'}


@prodect_controllar.put('/{title}')
def updata_topic(request,title):
 post.update(title.name)
 post.update(title.index)
 return{'massge':'your  update is seccessfull '}
@prodect_controllar.delete('/{title}')
def updata_topic(request,title):
    post.remove(title.name)
    return{'massge':'your  delete is seccessfull '}


# Create your views here.
