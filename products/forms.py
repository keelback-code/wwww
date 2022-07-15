from django import forms
from .models import Product


class HatOneForm(forms.ModelForm):
    """
    Form for designing a custom hat.
    """
    brim_width = [
        ('5', "5cm"),
        ('10', "10cm"),
        ('15', "15cm"),
    ]

    hat_height = [
        ('15', "15cm"),
        ('20', "20cm"),
        ('25', "25cm"),
    ]

    patch_choices = [
        ('STAR', "Star"),
        ('MOON', "Crescent moon"),
        ('PRIDE', "Pride flag"),
        ('TRANS', "Trans flag"),
        ('ANARCHY', "Anarchy patch"),
        ('NONE', "None"),
    ]

    variable_one = forms.ChoiceField(choices=brim_width)
    variable_two = forms.ChoiceField(choices=hat_height)
    variable_three = forms.ChoiceField(choices=patch_choices)

    class Meta:
        model = Product
        fields = ('color', 'stat', 'variable_one', 'variable_two', 'variable_three',)