from django.shortcuts import render
from .models import Post
from . forms import PostForm

# Create your views here.
def post_list(request):   
    all_post = Post.objects.all() ## data from model.
    #print (all_post)
    return render(request, 'post/all_posts.html',{'all_post':all_post})

def post_detail(request,id):
    post = Post.objects.get(id=id)
    return render(request,'post/one_post.html',{'post':post} )

def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form .is_valid():
            form.save()
    else:
        form = PostForm()
    return render(request,'post/post_create.html',{'form':form})


def post_edit(request,id):
    post = Post.objects.get(id=id)
    if request.method == "POST":
        form = PostForm(request.POST,instance=post)
        if form .is_valid():
            form.save()
    else:
        form =PostForm(instance=post)
    return render(request,'post/post_edit.html',{'form':form})                         



