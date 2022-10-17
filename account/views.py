from django.shortcuts import render
from account.models import *
import json

# Create your views here.

def home(request,*args,**kwargs):
    stories=[]
    for user in ProfileUser.objects.all():
        
        print(user)
        items=[]
        for status in user.status.all():
            items.append({
                "id": status.id,
                "type":"",
                "length":3,
                "src":f'/media/{status.file}',
           })

        stories.append({
            "id":str(user.id),
            "photo":f'/media/{user.photo}',
            "name":user.name,
            "items":items
        })    
    print(stories)      
    return render(request,"chatapp/home.html",{'context':json.dumps(stories)})

