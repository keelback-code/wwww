from django import forms
from .models import Product


class HatOneForm(forms.ModelForm):
    """
    Form for designing a custom hat.
    """
    brim_width = [
        ('Brim - 5cm', "5cm"),
        ('Brim - 10cm', "10cm"),
        ('Brim - 15cm', "15cm"),
    ]

    hat_height = [
        ('Height - 15cm', "15cm"),
        ('Height - 20cm', "20cm"),
        ('Height - 25cm', "25cm"),
    ]

    patch_choices = [
        ('Patch - Star', "Star"),
        ('Patch - Moon', "Crescent moon"),
        ('Patch - Pride flag', "Pride flag"),
        ('Patch - Trans flag', "Trans flag"),
        ('Patch - Anarchy', "Anarchy patch"),
        ('Patch - None', "None"),
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
        ('Spell - Freeze', "Freeze"),
        ('Spell - Wither', "Wither"),
        ('Spell - Overexplain', "Overexplain"),
    ]

    hat_floppiness = [
        ('Fairly floppy', "Fairly"),
        ('Very floppy', "Very floppy"),
        ('Very extremely floppy', "Very extremely floppy"),
    ]

    patch_choices_two = [
        ('Patch - Nonbinary flag', "Nonbinary flag"),
        ('Patch - Lesbian flag', "Lesbian flag"),
        ('Patch - Genderqueer flag', "Genderqueer flag"),
        ('Patch - Goose', "Goose"),
        ('Patch - Moose', "Moose"),
        ('Patch - None', "None"),
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
        ('Length - Mini', "Mini"),
        ('Length - Midi', "Midi"),
        ('Length - So Long You Will Step On It', "So Long You Will Step On It"),
    ]

    cloak_pattern = [
        ('Pattern - Tartan', "Tartan"),
        ('Pattern - Leaves', "Leaves"),
        ('Pattern - Bowling alley carpet', "Bowling alley carpet"),
    ]

    clasp_choices = [
        ('Clasp - LOTR Leaf clasp', "Leaf clasp"),
        ('Clasp - Two hands shaking', "Two hands shaking"),
        ('Clasp - Rainbow', "Rainbow"),
        ('Clasp - Snake', "Snake"),
        ('Clasp - None', "None"),
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
        ('Length - 10cm', "10cm"),
        ('Length - 15cm', "15cm"),
        ('Length - 20cm', "20cm"),
    ]

    wand_point = [
        ('Point - Cactus', "Cactus"),
        ('Point - Orb', "Orb"),
        ('Point - Ice Lolly', "Ice Lolly (never melts, not edible)"),
    ]

    starting_spells = [
        ('Spell - Crush', "Crush your enemies"),
        ('Spell - See', "See them driven before you"),
        ('Spell - Hear', "Hear the lamentation of the women"),
        ('Spell - None', "None"),
    ]

    variable_one = forms.ChoiceField(choices=wand_length, label="Length")
    variable_two = forms.ChoiceField(choices=wand_point, label="Pointy End")
    variable_three = forms.ChoiceField(choices=starting_spells, label="Starting Spell")

    class Meta:
        model = Product
        fields = ('color', 'stat', 'variable_one', 'variable_two', 'variable_three',)
