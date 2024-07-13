from django.contrib import admin
from .models import Collection, Stack
#cause Stack is stored in Collection

admin.site.register(Collection)
admin.site.register(Stack)