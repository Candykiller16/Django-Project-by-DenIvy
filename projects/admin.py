from django.contrib import admin
from .models import Project, Rewiew, Tag

# Register your models here.
admin.site.register(Project)
admin.site.register(Rewiew)
admin.site.register(Tag)