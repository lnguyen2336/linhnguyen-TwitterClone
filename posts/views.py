from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from .forms import PostForm

# Create your views here.

def index(request):
    # If the method is POST
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)    
        #If the form is valid
        if form.is_valid():
            # Yes, Save
            form.save()

            # Redirect to Home
            return HttpResponseRedirect('/')
        else:
            # No, Show Error
            return HttpResponseRedirect(form.errors.as_json())
        
    # Get all posts, limits = 20
    posts = Post.objects.all().order_by("-created_at")[:20]
    form = PostForm

    # Show
    return render(request, 'posts.html',
                    {'posts': posts})

def delete(request, post_id):
    # Find user
    post = Post.objects.get(id = post_id)
    post.delete()
    return HttpResponseRedirect('/')


def edit(request, post_id):
    post = Post.objects.get(id = post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect(form.errors.as_json())
    return render(request, 'edit.html',
                  {'post': post})

def like(request, post_id):
    post = Post.objects.get(id = post_id)
    new_value = post.likes+1
    post.likes = new_value
    post.save()
    return HttpResponseRedirect('/')
    