from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User


class Product(models.Model):
    """
    Model for generating and processing products.
    """
    stat_choices = [
        ('Courage', "Courage"),
        ('Cool', "Cool"),
        ('Sun Protection', "Sun Protection"),
        ('Spell Casting', "Spell Casting"),
        ('Stealth', "Stealth"),
    ]

    color_choices = [
        ('Purple', "Purple"),
        ('Navy', "Navy"),
        ('Pink', "Pink"),
        ('Green', "Green"),
        ('Orange', "Orange"),
    ]

    product_type = models.CharField(max_length=254, null=True, blank=True)
    stat = models.CharField(max_length=50, choices=stat_choices, default='COURAGE')
    price = models.IntegerField()
    color = models.CharField(max_length=20, choices=color_choices, default='PURPLE')
    variable_one = models.CharField(max_length=254, null=True, blank=True)
    variable_two = models.CharField(max_length=254, null=True, blank=True)
    variable_three = models.CharField(max_length=254, null=True, blank=True)


class StaffSubmission(models.Model):
    """
    Model for allowing staff to submit products and store the data.
    """
    staff_member = models.ForeignKey(User, on_delete=models.CASCADE)
    product_type = models.CharField(max_length=50, null=True, blank=True)
    stat = models.BooleanField(verbose_name="Include stats")
    color = models.BooleanField(verbose_name="Include colors")
    variable_one = models.CharField(max_length=50, null=True, blank=True)
    variable_one_option_one = models.CharField(max_length=254, null=True, blank=True)
    variable_one_option_two = models.CharField(max_length=254, null=True, blank=True)
    variable_one_option_three = models.CharField(max_length=254, null=True, blank=True)
    variable_two = models.CharField(max_length=50, null=True, blank=True)
    variable_two_option_one = models.CharField(max_length=254, null=True, blank=True)
    variable_two_option_two = models.CharField(max_length=254, null=True, blank=True)
    variable_two_option_three = models.CharField(max_length=254, null=True, blank=True)
    variable_three = models.CharField(max_length=50, null=True, blank=True)
    variable_three_option_one = models.CharField(max_length=254, null=True, blank=True)
    variable_three_option_two = models.CharField(max_length=254, null=True, blank=True)
    variable_three_option_three = models.CharField(max_length=254, null=True, blank=True)
    image = CloudinaryField('image', null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
