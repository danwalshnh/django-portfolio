from django.shortcuts import render
from journal.models import Post
# Create your views here.
def journal_index(request):
    posts = Post.objects.all().order_by('-created_on')
    context = {
        "posts": posts,
    }
    return render(request, "journal_index.html",context)

def journal_category(request, category):
    posts = Post.objects.filter(
        categories__name__contains=category
    ).order_by(
        '-created_on'
    )
    context = {
        "category": category,
        "posts": posts
    }
    return render(request, "journal_category.html", context)

def journal_detail(request, pk):
    post = Post.objects.get(pk=pk)
    context = {
        "post":post,
    }
    return render(request, "journal_detail.html", context)
