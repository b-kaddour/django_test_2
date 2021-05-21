from django.contrib import admin
from .models import Ingredient
from .models import Recette
from .models import Comment

# Register your models here.
class RecetteAdmin(admin.ModelAdmin):
    list_display = ('titre','description')

admin.site.register(Recette, RecetteAdmin)
admin.site.register(Ingredient)
admin.site.register(Comment)
