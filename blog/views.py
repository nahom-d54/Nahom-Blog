from django.shortcuts import render, get_object_or_404
from .models import Post
from django.contrib.auth.decorators import login_required
#blog views

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts,'year':'2023'})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post,'year':'2023'})

@login_required
def create_post(request):
    if request.user.is_authenticated:
        return render(request,'blog/post_maker.html',{'post':'create post','year':'2023'})