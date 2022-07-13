import random
import string
from django.db import models


def random_sku_generator(chars=string.ascii_lowercase + string.digits):
    """
    Function for creating a random sku.
    """
    return ''.join(random.choice(chars) for _ in range(6))


class CustomProduct(models.Model):
    """
    Model for custom products.
    """
    sku = models.CharField(max_length=254, null=True, blank=True)
    brim_width = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    hat_height = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    color = models.CharField(max_length=254, null=True, blank=True)
    patch = models.CharField(max_length=254, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)  # or in views?

    def calc_price(self):
        """
        Function to calculate the cost of the customised hat.
        """
        # self.price = 0

        if self.brim_width == "1":
            self.price = self.price + 5
        elif self.brim_width == "2":
            self.price = self.price + 10
        elif self.brim_width == "3":
            self.price = self.price + 15
        else:
            self.price = self.price + 0
        
        if self.hat_height == "1":
            self.price = self.price + 5
        elif self.hat_height == "2":
            self.price = self.price + 10
        elif self.hat_height == "3":
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
        self.slug = random_sku_generator()
        super().save(*args, **kwargs)
