from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comments
from .forms import PostForm, CommentForm

def index(request):
    posts = Post.objects.all().order_by('-datePosted')
    comments = Comments.objects.all()
    context = {
        'posts' : posts,
    }
    return render(request, 'posts/index.html', context)

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

def postDetail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = Comments.objects.filter(post=post)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
            return redirect('postDetail', post_id=post_id)
    else:
        form = CommentForm
    context = {
        'post' : post,
        'comments' : comments,
        'form' : form
    }
    return render(request, 'posts/postDetail.html', context)