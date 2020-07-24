from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import *
from .forms import * 

# Create your views here.

def home(request):
    blog = BlogModel.objects.all()
    form = BlogForm()
    if(request.method == 'POST'):
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'blog':blog, 'form':form}
    # return HttpResponse('Hwllo World')
    return render(request,'blog/home.html',context) 


# delete view for details 
# def deletelist(request, id): 
    
#     # fetch the object related to passed id 
#     blog = get_object_or_404(BlogModel, id = id) 
#     if request.method =="POST": 
#         # delete object 
#         blog.delete() 
#         # after deleting redirect to home page 
#         return redirect("/") 
#     context = {}
#     return render(request, "blog/deletelist.html", context) 

def deletelist(request, id): 
    # fetch the object related to passed id 
    blog = get_object_or_404(BlogModel, id = id) 
    if request.method =="POST": 
        # delete object 
        blog.delete() 
        # after deleting redirect to home page 
        return redirect("/") 
    context = {}
    return render(request, "blog/deletelist.html", context) 


def updatelist(request, id): 
    # dictionary for initial data with field names as keys 
     
    # fetch the object related to passed id 
    blog = get_object_or_404(BlogModel, id = id)  
    form = BlogForm(instance = blog)
    if(request.method == 'POST'):
        form = BlogForm(request.POST, instance = blog)
        if form.is_valid():
            form.save()
        return redirect('/')
    context ={'form':form}
    return render(request,'blog/updatedata.html',context)
  