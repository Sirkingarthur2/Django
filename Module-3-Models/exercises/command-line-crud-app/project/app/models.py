from django.db import models

# Create your models here.

class Palette(models.Model):
    name = models.CharField(max_length=30)
    colors = models.TextField()
    favorite_colors = models.BooleanField() 

def create(name, colors, favorite_colors):
    new_palette = Palette.objects.create(name=name, colors=colors, favorite_colors=favorite_colors)
    return new_palette

def read_all():
    return Palette.objects.all()

def search_by_name(name):
    try:
        return Palette.objects.get(name=name)
    except Palette.DoesNotExist:
        return None

def read_favorites():
    return Palette.objects.filter(favorite_colors=True)

def update(name, new_colors, new_favorite_status):
    try:
        palette = Palette.objects.get(name=name)
        palette.colors = new_colors
        palette.favorite_colors = new_favorite_status
        palette.save()
        return palette
    except Palette.DoesNotExist:
        return None

def delete(name):
    try:
        palette = Palette.objects.get(name=name)
        palette.delete()
        return True
    except Palette.DoesNotExist:
        return False
