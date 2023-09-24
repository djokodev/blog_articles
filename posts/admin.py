from django.contrib import admin
from .models import BlogPost


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "slug", "date", "published"]
    list_editable = ("published", ) #permet d'editer directement certain champ a l'interieur de l'interface d'admin


admin.site.register(BlogPost, BlogPostAdmin)
