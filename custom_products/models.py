import random
import string
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


def random_sku_generator(chars=string.ascii_lowercase + string.digits):
    """
    Function for creating a random sku.
    """
    return ''.join(random.choice(chars) for _ in range(6))


class CustomProduct(models.Model):
    """
    Model for custom products.
    """
    color_choices = [
        ('PURPLE', "Purple"),
        ('NAVY', "Navy"),
        ('PINK', "Pink"),
        ('GREEN', "Green"),
        ('ORANGE', "Orange"),
    ]

    patch_choices = [
        ('STAR', "Star"),
        ('MOON', "Crescent moon"),
        ('PRIDE', "Pride flag"),
        ('TRANS', "Trans flag"),
        ('ANARCHY', "Anarchy patch"),
    ]

    sku = models.CharField(max_length=254, null=True, blank=True)
    brim_width = models.IntegerField(default=5, validators=[MinValueValidator(5), MaxValueValidator(20)], null=True, blank=True)
    hat_height = models.IntegerField(default=20, validators=[MinValueValidator(20), MaxValueValidator(35)], null=True, blank=True)
    color = models.CharField(max_length=254, choices=color_choices, default='PURPLE')
    patch = models.CharField(max_length=254, choices=patch_choices, default='STAR', null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)  # or in views?

    def calc_price(self):
        """
        Function to calculate the cost of the customised hat.
        """
        # self.price = 0

        if self.brim_width >= 10:
            self.price = self.price + 5
        elif self.brim_width >= 15:
            self.price = self.price + 10
        elif self.brim_width >= 20:
            self.price = self.price + 15
        else:
            self.price = self.price + 0
        
        if self.hat_height >= 25:
            self.price = self.price + 5
        elif self.hat_height >= 30:
            self.price = self.price + 10
        elif self.hat_height >= 35:
            self.price = self.price + 15
        else:
            self.price = self.price + 0
        
        if self.patch is True:
            self.price = self.price + 2
        else:
            self.price = self.price + 0
        
        print(self.price)
        return self.price
    

    def save(self, *args, **kwargs):
        """
        Function for saving while generating a random sku.
        """
        self.sku = random_sku_generator()
        super().save(*args, **kwargs)
