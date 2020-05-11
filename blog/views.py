from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'Author 1',
        'title': 'First Post',
        'content': 'Content of Blog 1',
        'date_published': '11 May, 2020'
    },
    {
        'author': 'Author 2',
        'title': 'Second Post',
        'content': 'Content of Blog 2',
        'date_published': '12 May, 2020'
    },
    {
        'author': 'Author 3',
        'title': 'Third Post',
        'content': 'Content of Blog 3',
        'date_published': '13 May, 2020'
    }
]

# Create your views here.
def home(request):
    context = {
        'posts': posts,
        'title': 'Home',
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})