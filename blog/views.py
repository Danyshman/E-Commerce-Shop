from django.shortcuts import render
from .models import Blog
from django.shortcuts import get_object_or_404


def detail_blog(request, id):
    if request.method == 'GET':
        blog = get_object_or_404(klass=Blog, pk=id)
        context = {
            "blog_detail": blog
        }
        return render(request, 'blog/blog-single.html', context)

