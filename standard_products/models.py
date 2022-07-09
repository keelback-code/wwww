from django.db import models


class Stat(models.Model):
    """
    Model for categorising and filtering the standard products.
    Based on Code Institute Boutique Ado project.
    """
    class Meta:
        verbose_name_plural = 'Stats'
        
    name = models.CharField(max_length=100)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class StandardProduct(models.Model):
    """
    Model for standard products.
    """
    stat = models.ForeignKey('Stat', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(null=True, blank=True)
    stock_level = models.IntegerField(default=0)
    # stat_category_one = models.CharField(max_length=254, null=True, blank=True)
    # stat_number_one = models.IntegerField(null=True, blank=True)
    # stat_category_two = models.CharField(max_length=254, null=True, blank=True)
    # stat_number_two = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name
