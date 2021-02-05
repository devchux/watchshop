from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Post

# Create your views here.
def bloghome(request):
    post_list = Post.objects.all()
    recent_post = post_list[:5]
    paginator = Paginator(post_list, 2)
    page_number = request.GET.get('page')
    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {
        'title': 'Blog',
        'page_number': page_number,
        'posts': posts,
        'recent_post': recent_post
    }
    return render(request, 'blog/blog.html', context)

def blog_detail(request, pk):
    post = Post.objects.get(id=pk)
    post_count = Post.objects.all().count()
    recent_post = Post.objects.all()[:5]
    prev = pk - 1
    nex = pk + 1
    print(post)
    if pk == 1:

        try:
          next_post = Post.objects.get(id=nex)
          context = {
                'title': 'Post Details',
                'post': post,
                'next_post': next_post,
                'recent_post': recent_post
            }
        except Exception:
            context = {
                'title': 'Post Details',
                'post': post,
                'recent_post': recent_post
            }

    elif pk > 1 and pk < post_count:
        prev_post = Post.objects.get(id=prev)
        next_post = Post.objects.get(id=nex)

        context = {
                'title': 'Post Details',
                'post': post,
                'prev_post': prev_post,
                'next_post': next_post,
                'recent_post': recent_post
        }
    
    elif pk == post_count:
        prev_post = Post.objects.get(id=prev)

        context = {
                'title': 'Post Details',
                'post': post,
                'prev_post': prev_post,
                'recent_post': recent_post
        }
    return render(request, 'blog/blog-details.html', context)