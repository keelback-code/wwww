import random
import string
from django.db import models

def random_sku_generator(chars=string.ascii_lowercase + string.digits):
    """
    Function for creating a random sku.
    """
    return ''.join(random.choice(chars) for _ in range(8))


class Product(models.Model):
    """
    Model for generating and processing products.
    """
    stat_choices = [
        ('COURAGE', "Courage"),
        ('COOL', "Cool"),
        ('SUN_PROTECTION', "Sun Protection"),
        ('SPELL_CASTING', "Spell Casting"),
        ('STEALTH', "Stealth"),
    ]

    color_choices = [
        ('PURPLE', "Purple"),
        ('NAVY', "Navy"),
        ('PINK', "Pink"),
        ('GREEN', "Green"),
        ('ORANGE', "Orange"),
    ]

    sku = models.CharField(max_length=254, null=True, blank=True)
    stat = models.CharField(max_length=50, choices=stat_choices, default='COURAGE')
    price = models.IntegerField()
    color = models.CharField(max_length=20, choices=color_choices, default='PURPLE')
    variable_one = models.CharField(max_length=254, null=True, blank=True)
    variable_two = models.CharField(max_length=254, null=True, blank=True)
    variable_three = models.CharField(max_length=254, null=True, blank=True)

    def save(self, *args, **kwargs):
        """
        Function for generating a random sku.
        """
        self.sku = random_sku_generator()
        super().save(*args, **kwargs)
        return self.sku
