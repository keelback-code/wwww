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

    variable_one = forms.ChoiceField(choices=brim_width, label="Brim Width")
    variable_two = forms.ChoiceField(choices=hat_height, label="Hat Height")
    variable_three = forms.ChoiceField(choices=patch_choices, label="Patch Options")

    class Meta:
        model = Product
        fields = ('color', 'stat', 'variable_one', 'variable_two', 'variable_three',)


class HatTwoForm(forms.ModelForm):
    """
    Form for designing a custom hat.
    """
    spell_choices = [
        ('A', "Freeze"),
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

    variable_one = forms.ChoiceField(choices=spell_choices, label="Built-in Spell Options")
    variable_two = forms.ChoiceField(choices=hat_floppiness, label="Hat Floppiness")
    variable_three = forms.ChoiceField(choices=patch_choices_two, label="Patch Options")

    class Meta:
        model = Product
        fields = ('color', 'stat', 'variable_one', 'variable_two', 'variable_three',)
    

class CloakForm(forms.ModelForm):
    """
    Form for designing a custom cloak.
    """
    cloak_length = [
        ('A', "Mini"),
        ('B', "Midi"),
        ('C', "So Long You'll Step On It"),
    ]

    cloak_pattern = [
        ('A', "Tartan"),
        ('B', "Leaves"),
        ('C', "Bowling alley carpet"),
    ]

    clasp_choices = [
        ('LOTR', "Leaf clasp"),
        ('SHAKE', "Two hands shaking"),
        ('RBOW', "Rainbow"),
        ('SNAKE', "Snake"),
        ('NONE', "None"),
    ]

    variable_one = forms.ChoiceField(choices=cloak_length, label="Length")
    variable_two = forms.ChoiceField(choices=cloak_pattern, label="Pattern")
    variable_three = forms.ChoiceField(choices=clasp_choices, label="Clasp")

    class Meta:
        model = Product
        fields = ('color', 'stat', 'variable_one', 'variable_two', 'variable_three',)


class WandForm(forms.ModelForm):
    """
    Form for designing a custom wand.
    """
    wand_length = [
        ('A', "10cm"),
        ('B', "15cm"),
        ('C', "20cm"),
    ]

    wand_point = [
        ('A', "Cactus"),
        ('B', "Orb"),
        ('C', "Ice lolly (never melts, not edible)"),
    ]

    starting_spells = [
        ('CRUSH', "Crush your enemies"),
        ('SEE', "See them driven before you"),
        ('HEAR', "Hear the lamentation of the women"),
        ('NONE', "None"),
    ]

    variable_one = forms.ChoiceField(choices=wand_length, label="Length")
    variable_two = forms.ChoiceField(choices=wand_point, label="Pointy End")
    variable_three = forms.ChoiceField(choices=starting_spells, label="Starting Spell")

    class Meta:
        model = Product
        fields = ('color', 'stat', 'variable_one', 'variable_two', 'variable_three',)
