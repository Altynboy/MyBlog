from django.shortcuts import render
from django.http import HttpResponse

post = [
    {
        'author': 'Altyn',
        'title': 'First Post',
        'content': 'Let\'s get it',
        'date_posted': '1488'
    },
    {
        'author': 'Arthas',
        'title': 'Second Post',
        'content': 'НЫАААА!',
        'date_posted': '4:20'
    }
]

def blog(request):
    context = {
        'posts': post
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})


def bootstrap_test(request):
    return render(request, 'blog/bootstraptest.html')
