from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# posts = [
#     {
#         'title': 'First Post',
#         'author': 'Author 1',
#         'content': 'Content of Blog 1',
#         'date_published': '11 May, 2020'
#     },
#     {
#         'title': 'Second Post',
#         'author': 'Author 2',
#         'content': 'Content of Blog 2',
#         'date_published': '12 May, 2020'
#     },
#     {
#         'title': 'Third Post',
#         'author': 'Author 3',
#         'content': 'Content of Blog 3',
#         'date_published': '13 May, 2020'
#     }
# ]

# Create your views here.
def home(request):
    context = {
        'posts': Post.objects.all(),
        'title': 'Home',
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})