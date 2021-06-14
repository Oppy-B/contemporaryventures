from django.shortcuts import render
from django.conf import settings
from .forms import PostForm
from django.http import Http404,HttpResponseRedirect
from .models import (Category,Post,)
from django.core.paginator import Paginator
from django.db.models import Q

import os
# Create your views here.


def blog_index(request):
    post_list = Post.objects.all().order_by('-created_on')
    query = request.GET.get('q')
    category_list = Category.objects.all()
    first_3_post = Post.objects.all().order_by('-created_on')[:3]
    if query:
        post_list = post_list.filter(
            Q(title__icontains=query) |
            Q(body__icontains=query)
                
                     
            )
    paginator = Paginator(post_list, 5) # Show 3 contacts per page.
    page_request_var = 'page'
    page_number = request.GET.get(page_request_var)
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj' : page_obj,
        'page_request_var' : page_request_var,
        'category_list' : category_list,
        'first_3_post' : first_3_post
    }
    return render(request, "blog/blog_index.html", context)
    

def blog_category(request, category):
    posts = Post.objects.filter(
        categories__name__contains=category
    ).order_by('-created_on')
    category_list = Category.objects.all()
    first_3_post = Post.objects.all().order_by('-created_on')[:3]
    context = {
        'category' : category,
        'posts' : posts,
        'category_list' : category_list,
        'first_3_post' : first_3_post
    }
    return render(request, 'blog/blog_category.html', context)

def blog_detail(request, slug):
    post = Post.objects.filter(slug__iexact=slug)
    post = post.first()
    category_list = Category.objects.all()
    first_3_post = Post.objects.all().order_by('-created_on')[:3]
    context = {
        'post' : post,
        'category_list' : category_list,
        'first_3_post' : first_3_post
    }
    
    return render(request, 'blog/blog_details.html', context)

def blog_create(request):
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            form = PostForm()
            return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        'form':form ,
        
    }
    return render(request, 'blog/blog_create.html', context)