from django.shortcuts import render
from .models import Blog
from django.shortcuts import get_object_or_404


def detail_blog(request, id):
    if request.method == 'GET':
        print('in view')
        print(id)
        blog = get_object_or_404(klass=Blog, pk=id)
        print(blog.main_img)
        context = {
            "blog_detail": blog
        }
        return render(request, 'blog/blog-single.html', context)

