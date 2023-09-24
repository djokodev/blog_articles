from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth import get_user_model

User = get_user_model() #recupere le model d'utilisateur de notre application

class BlogPost(models.Model):
    title = models.CharField(max_length=255, unique=True, verbose_name="Titre")
    
    """versio du titre qui vas etre utiliser a 
    l'interieur des urls pour pouvoir acceder a nos articles"""
    slug = models.SlugField(max_length=255, unique=True, blank=True) 
    
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="auteur")
    date = models.DateTimeField(auto_now=True, verbose_name="date de creation")
    published = models.BooleanField(default=False, verbose_name="Publié")
    content = models.TextField()
    
    class Meta:
        ordering = ["-date"] #Permet d'ordonne les article publier par les plus rescent
        verbose_name = "Article" #affiche dans l'admin le nom de notre model Article au lieu de BlogPost
        
        
    def __str__(self):
        return self.title
    
    """on surchage la methode save pcq on veut que si l'utilisateur ne specifie pas un slug on prend le titre de 
       l'article et on le slugifi quoi! """
    def save(self, *args, **kwargs):
        
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)