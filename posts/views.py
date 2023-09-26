from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from .models import BlogPost
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


"""ListView est une vue basée sur une classe dans Django qui facilite l'affichage 
    d'une liste d'objets d'un modèle spécifique. """
class BlogHome(ListView): 
    model= BlogPost
    template_name = "posts/home.html"
    context_object_name = "posts" #nom a utiliser dans le template associer
    paginate_by = 4

@method_decorator(login_required, name='dispatch')
class BlogPostCreate(CreateView):
    model = BlogPost
    template_name = "posts/create_post.html"
    fields = ["title", "picture", "content", ] #determine les champs a afficher dans le formulaire qui vas etre retourne par CreateView
    
@method_decorator(login_required, name='dispatch')
class BlogPostUpdate(UpdateView):
    model = BlogPost
    template_name = "posts/update_post.html"
    fields = ["title", "picture", "content", ]
    
    
class BlogPostDetail(DetailView):
    model = BlogPost
    context_object_name = "posts"
    template_name = "posts/detail_post.html"
    
    
    
    """specifie ou sera rediriger l'utilisateur apres sa suppression vu que
        deleteView de prends pas en compte get_absolute_url comme createView et UpdateView.""" 
@method_decorator(login_required, name='dispatch')
class BlogPostDelete(DeleteView):
    model = BlogPost
    template_name = "posts/delete_post.html"
    context_object_name = "posts"
    success_url = reverse_lazy("home")
   