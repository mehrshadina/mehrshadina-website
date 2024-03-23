from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
from django.http import HttpResponseRedirect
from blog.forms import CommentForm
from django.db.models import Count
from django.db.models.functions import TruncMonth

def post_list(request):
    # Filter posts by year and month
    posts = Post.objects.all()
    
    # Fetch archives for navigation
    archives = Post.objects.annotate(
        year_month=TruncMonth('pub_date')
    ).values('year_month').annotate(
        count=Count('id')
    ).order_by('-year_month')
    
    context = {
        "posts": posts,
        "archives": archives,
    }
    return render(request, 'blog/post_archive.html', context=context)

def post_archive(request, year, month):
    # Filter posts by year and month
    posts = Post.objects.filter(pub_date__year=year, pub_date__month=month)
    
    # Fetch archives for navigation
    archives = Post.objects.annotate(
        year_month=TruncMonth('pub_date')
    ).values('year_month').annotate(
        count=Count('id')
    ).order_by('-year_month')
    
    context = {
        "posts": posts,
        "archives": archives,
    }
    return render(request, 'blog/post_archive.html', context=context)

def post_detail(request, pk):
    recent_posts = Post.objects.values_list('title', flat=True)
    post = Post.objects.get(pk=pk)
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post,
            )
            comment.save()
            return HttpResponseRedirect(request.path_info)
    
    archives = Post.objects.annotate(
        year_month=TruncMonth('pub_date')
    ).values('year_month').annotate(
        count=Count('id')
    ).order_by('-year_month')

    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "recent_posts": recent_posts,
        "archives": archives,
        "comments": comments,
        "form": CommentForm(),
    }
    return render(request, 'blog/post_detail.html', context=context)


def blog_category(request, category):
    posts = Post.objects.filter(
        categories__name__contains=category
    )
    context = {
        "category": category,
        "posts": posts,
    }
    return render(request, "blog/category.html", context)