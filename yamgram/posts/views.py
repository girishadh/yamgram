from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm

def index(request):
    posts = Post.objects.all().order_by('-datePosted')
    return render(request, 'posts/index.html', {'posts':posts})

def postCreate(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('index')
    else:
        form = PostForm
    return render(request, 'posts/postCreate.html', {'form':form})

def like(request, post_id):
    if not request.user.is_authenticated:
        return redirect('login')
    post = Post.objects.get(id=post_id)
    post.likes.add(request.user)
    post.dislikes.remove(request.user)
    return redirect('index')

def dislike(request, post_id):
    if not request.user.is_authenticated:
        return redirect('login')
    post = Post.objects.get(id=post_id)
    post.dislikes.add(request.user)
    post.likes.remove(request.user)
    return redirect('index')