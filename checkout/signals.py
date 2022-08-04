from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import OrderLineItem
"""
Signal for checkout objects,
based on Code Institute's Boutique Ado walkthrough.
"""


@receiver(post_save, sender=OrderLineItem)
def update_on_save(sender, instance, created, **kwargs):
    """
    Handles signals from post_save event/update
    order total on linetem update/create
    """
    instance.order.update_total()


@receiver(post_delete, sender=OrderLineItem)
def update_on_delete(sender, instance, **kwargs):
    """
    Update order total on lineitem delete
    """
    instance.order.update_total()
