from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView
from django.views.generic import CreateView, UpdateView
from django.http import HttpResponseRedirect
# Create your views here.
from .models import Post
from .models import Category

class BlogListView(ListView):
    model = Post
    template_name = "home.html"

class BlogDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"

# class BlogCreateView(CreateView):
#     model = Post
#     template_name = "post_new.html"
#     fields = ['title','author','content','img','category']

# def create(request):
#     categories = Category.objects.all()
#     if request.method == "POST":
#         title = request.POST.get('title')
#         content = request.POST.get('content')
#         category = request.POST.get('category')
#         img = request.FILES.get('img')
#         ctg = Category.objects.get(id=category)

#         post = Post(title=title, content=content, category = ctg, img=img, author = request.user)
#         post.save()

#         return render(request, 'post_new.html',{"catego":categories})

def create(request):
    categores = Category.objects.all()
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        category = request.POST.get('category')
        img = request.FILES.get('img')
        ctg = Category.objects.get(id=category)
        blog = Post(title=title,content=content,category=ctg,img=img,author=request.user)
        blog.save()

    return render(request,'post_new.html',{"catego":categores})