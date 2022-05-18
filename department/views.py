from django.shortcuts import render
from . models import Post

# Create your views here.
#GET and POST HTTP protocol

def homepage(request):
	return render(request, 'index.html', {"post": Post.objects.all})























