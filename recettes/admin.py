from django.contrib import admin
from .models import Recette
from .models import Ingredient

# Register your models here.
class RecetteAdmin(admin.ModelAdmin):
    list_display = ('titre','description')

admin.site.register(Recette, RecetteAdmin)
admin.site.register(Ingredient)
