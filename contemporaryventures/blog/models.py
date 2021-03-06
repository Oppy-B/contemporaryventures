from django.db import models

from django.urls import reverse
from django.db.models.signals import pre_save
from django.utils.text import slugify

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

def upload_location(instance, filename):
    return "%s/%s" %(instance.id, filename)

class Post(models.Model):

    title = models.CharField(max_length=255)
    image = models.ImageField(blank=True, null=True, 
            upload_to= upload_location, 
            height_field="height_field", 
            width_field="width_field")
    height_field = models.IntegerField(default=0, blank=True, null=True)
    width_field = models.IntegerField(default=0, blank=True, null=True)
    slug = models.SlugField(unique=True, null=True)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField('Category', related_name='posts')

    

    def get_absolute_url(self):
        return reverse('blog:blog_detail', kwargs={'slug':self.slug})

def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = Post.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)


pre_save.connect(pre_save_post_receiver, sender=Post)