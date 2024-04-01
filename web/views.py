from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from web.models import Expense, Income, Token, User
from json import JSONEncoder
from datetime import datetime
from django.shortcuts import render, redirect
from .models import Project
from .forms import ProjectForm
from django.contrib import messages
from blog.models import Post
from django.db.models import Count
from django.db.models.functions import TruncMonth

# Create your views here.
def index(request):
    posts = Post.objects.all()
    context= {'posts': posts}
    #return HttpResponse("Hello, world. You're at the web index.")
    return render(request, 'index.html', context)

def contact(request):
    recent_posts = Post.objects.values_list('pk', 'title')
    archives = Post.objects.annotate(
        year_month=TruncMonth('pub_date')
    ).values('year_month').annotate(
        count=Count('id')
    ).order_by('-year_month')

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

    context= {
        'recent_posts': recent_posts,
        'archives': archives
    }
    return render(request, 'contact.html', context)

def about(request):
    recent_posts = Post.objects.values_list('pk', 'title')
    archives = Post.objects.annotate(
        year_month=TruncMonth('pub_date')
    ).values('year_month').annotate(
        count=Count('id')
    ).order_by('-year_month')

    context= {
        'recent_posts': recent_posts,
        'archives': archives
    }
    return render(request, 'about.html', context)

def donate(request):
    recent_posts = Post.objects.values_list('pk', 'title')
    archives = Post.objects.annotate(
        year_month=TruncMonth('pub_date')
    ).values('year_month').annotate(
        count=Count('id')
    ).order_by('-year_month')

    context= {
        'recent_posts': recent_posts,
        'archives': archives
    }
    return render(request, 'donate.html', context)

def project_order(request):
    context= {}
    return render(request, 'project_order.html', context)

def tutoring(request):
    context= {}
    return render(request, 'tutoring.html', context)

def projects(request):
    context= {}
    return render(request, 'projects.html', context)

@csrf_exempt
def submit_expense(request):
    """ submit an expense"""
    #TODO: validate date, user might be fake, token might be fake, amount might be invalid
    this_token = request.POST['token']
    this_user = User.objects.filter(token__token=this_token).get()
    Expense.objects.create(
        user=this_user,
        amount=request.POST['amount'],
        text=request.POST['text'],
        date=datetime.now(), #TODO user might want submit date herself
    )
    return JsonResponse(
        {'status': 'ok',},
        encoder=JSONEncoder
    )

@csrf_exempt
def submit_income(request):
    """ submit an income"""
    print(request.POST)
    #TODO: validate date, user might be fake, token might be fake, amount might be invalid
    this_token = request.POST['token']
    this_user = User.objects.filter(token__token=this_token).get()
    Income.objects.create(
        user=this_user,
        amount=request.POST['amount'],
        text=request.POST['text'],
        date=datetime.now(), #TODO user might want submit date herself
    )
    return JsonResponse(
        {'status': 'ok',},
        encoder=JSONEncoder
    )

#@csrf_exempt
def create_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'پروژه با موفقیت ثبت شد.')
            return JsonResponse({'status': 'success'})

    else:
        form = ProjectForm()

    return render(request, 'create_project.html', {'form': form})
