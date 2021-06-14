from django.urls import path
from . import views


app_name = 'blog'

urlpatterns = [

    path("", views.blog_index, name = "blog_index"),
    path("<category>/", views.blog_category, name = "blog_category"),
    path("detail/<slug:slug>/", views.blog_detail, name = "blog_detail"),
    path("post/add/", views.blog_create, name ="blog_create"),

]