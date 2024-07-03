from django.contrib import admin

# Register your models here.
from api.models import Note

admin.site.register(Note)