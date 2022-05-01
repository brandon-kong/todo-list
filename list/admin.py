from django.contrib import admin

from .models import Item, User, List
# Register your models here.

admin.site.register(User)
admin.site.register(Item)
admin.site.register(List)