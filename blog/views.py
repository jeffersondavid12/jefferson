from django.shortcuts import render, get_object_or_404
from.models import category as a
from.models import post


# Create your views here
def blog(request):

    posts = post.objects.all()
    return render(request, 'blog/blog.HTML', {'posts': posts})

def category(request, category_id):

    category= a.objects.filter(id=category_id)
    return render(request, 'blog/category.HTML', {'category': category})