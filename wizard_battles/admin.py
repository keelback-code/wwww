from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    """
    Class for seeing wizard battle posts in the Django Admin.
    """
    list_display = ("title", "author",)

admin.site.register(Post, PostAdmin)
