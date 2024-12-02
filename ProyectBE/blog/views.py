#from django.shortcuts import render
#rom blog.models import Post

# Create your views here.

#def blog(request):
    
 #    posts=Post.objects.all()
  #   return render(request,"blog/blog.html", {"posts": posts } )
from rest_framework import viewsets
from .models import Categoria, Post
from .serializer import CategoriaSerializer, PostSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
