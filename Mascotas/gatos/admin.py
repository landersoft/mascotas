from django.contrib import admin
from .models import Gato



class AdminGato(admin.ModelAdmin):
    list_display = ["id","nombre","raza","nacimiento","sexo"]
    list_filter = ["raza"]
    search_fields = ["nombre", "sexo"]


# Register your models here.
admin.site.register(Gato, AdminGato)
