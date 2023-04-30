from django.contrib import admin

# Register your models here.
from .models import Menu, Boking

admin.site.register(Menu)
admin.site.register(Boking)