from django import forms
from .models import Product


class HatOneForm(forms.ModelForm):
    """
    Form for designing a custom hat.
    """
    brim_width = [
        ('A', "5cm"),
        ('B', "10cm"),
        ('C', "15cm"),
    ]

    hat_height = [
        ('A', "15cm"),
        ('B', "20cm"),
        ('C', "25cm"),
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


class HatTwoForm(forms.ModelForm):
    """
    Form for designing a custom hat.
    """
    spell_choices = [
        ('A', "Grow"),
        ('B', "Whither"),
        ('C', "Overexplain"),
    ]

    hat_floppiness = [
        ('A', "Fairly"),
        ('B', "Very floppy"),
        ('C', "Very extremely floppy"),
    ]

    patch_choices_two = [
        ('NONBINARY', "Nonbinary flag"),
        ('LESBIAN', "Lesbian flag"),
        ('GENDERQUEER', "Genderqueer flag"),
        ('GOOSE', "Goose"),
        ('MOOSE', "Moose"),
        ('NONE', "None"),
    ]

    variable_one = forms.ChoiceField(choices=spell_choices)
    variable_two = forms.ChoiceField(choices=hat_floppiness)
    variable_three = forms.ChoiceField(choices=patch_choices_two)

    class Meta:
        model = Product
        fields = ('color', 'stat', 'variable_one', 'variable_two', 'variable_three',)