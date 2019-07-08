from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def blog_index(request):
    return render(request, 'blog/blog_index.html')
