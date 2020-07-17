from django.shortcuts import render
from .models import Post
from .forms import PostForm

def index(request):
    posts = Post.objects.all()
    return render(request, 'index/index.html', {'abc': posts})

def new_post(request):
    form = PostForm(request.POST)
    if form.is_valid():
        post = form.save(commit=False)
        post.save()
    return render(request, 'index/new_post.html', {'form1': form})
