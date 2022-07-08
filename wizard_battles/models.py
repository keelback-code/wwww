from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User


class Post(models.Model):
    """
    Class for modelling wizard battle posts.
    """
    slug = models.SlugField(unique=True, primary_key=True)
    title = models.CharField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="battle_posts")
    text_content = models.TextField()
    image_one = models.ImageField(null=True, blank=True, default="placeholder_one")
    image_two = models.ImageField(null=True, blank=True, default="placeholder_two")

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("view_battle", kwargs={"slug": self.slug})

    # def save(self, *args, **kwargs):
    #     if not self.slug:
    #         self.slug = slugify(self.title)
    #     else:
    #         self.slug = self.slug
    #     return super().save(*args, **kwargs)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        else:
            self.slug = self.slug
        return super().save(*args, **kwargs)
    

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    comment_body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']
    
    def __str__(self):
        return f"Comment {self.comment_body} by {self.name}"
