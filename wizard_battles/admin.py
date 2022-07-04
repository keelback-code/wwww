from django.contrib import admin
from .models import Post, Comment


class PostAdmin(admin.ModelAdmin):
    """
    Class for seeing wizard battle posts in the Django Admin.
    """
    list_display = ("title", "author",)


class CommentAdmin(admin.ModelAdmin):
    """
    Class for seeing comments in the Django Admin.
    """
    list_display = ("name",)


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
