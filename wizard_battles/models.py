from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Post(models.Model):
    """
    Class for modelling wizard battle posts.
    """
    slug = models.SlugField(unique=True, primary_key=True)
    title = models.CharField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text_content = models.TextField()
    image_one = models.ImageField(null=True, blank=True, default="placeholder_one")
    image_two = models.ImageField(null=True, blank=True, default="placeholder_two")

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("wizard_battle", kwargs={"slug": self.slug})
