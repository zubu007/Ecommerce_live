from django.contrib import admin
from .models import Data

class DataAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'stars', 'price', 'image', 'category')

# Register your models here.

admin.site.register(Data, DataAdmin)
