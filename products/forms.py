from django import forms
from .models import Product, StaffSubmission


class StaffSubmissionForm(forms.ModelForm):
    class Meta:
        model = StaffSubmission
        exclude = ('staff_member', 'created_on',)


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


class SunglassesForm(forms.ModelForm):
    """
    Form for designing custom sunglasses
    """
    shape = [
        ('Shape - Heart', "Heart"),
        ('Shape - Sports Dad', "Sports Dad (unisex)"),
        ('Shape - Bubble', "Bubble"),
    ]

    beam_abilities = [
        ('Beam - Woodcutter', "Woodcutter"),
        ('Beam - Laser', "Laser"),
        ('Beam - Super Vision', "Super Vision"),
    ]

    lens_color = [
        ('Lens - Metallic', "Metallic"),
        ('Lens - Sunrise', "Sunrise"),
        ('Lens - Rainbow', "Rainbow"),
        ('Lens - None', "None"),
    ]

    variable_one = forms.ChoiceField(choices=shape, label="Shape")
    variable_two = forms.ChoiceField(choices=beam_abilities, label="Beam Abilities")
    variable_three = forms.ChoiceField(choices=lens_color, label="Lens Colors")

    class Meta:
        model = Product
        fields = ('color', 'stat', 'variable_one', 'variable_two', 'variable_three',)


class SpellBookForm(forms.ModelForm):
    """
    Form for designing custom sunglasses
    """
    cover = [
        ('Cover - Felt', "Felt"),
        ('Cover - Pineapple Leather', "Pineapple Leather"),
        ('Cover - School Backpacks', "School Backpacks"),
    ]

    first_spell = [
        ('First Spell - Make Sticky', "Make Sticky"),
        ('First Spell - Clean Dishes', "Clean Dishes"),
        ('First Spell - Start Car Alarm', "Start Car Alarm"),
    ]

    second_spell = [
        ('Second Spell - Mess up Hair', "Mess up Hair"),
        ('Second Spell - Remove Legs', "Remove Legs"),
        ('Second Spell - Disintegrate', "Disintegrate"),
        ('Second Spell - None', "None"),
    ]

    variable_one = forms.ChoiceField(choices=cover, label="Cover")
    variable_two = forms.ChoiceField(choices=first_spell, label="First Spell")
    variable_three = forms.ChoiceField(choices=second_spell, label="Second Spell")

    class Meta:
        model = Product
        fields = ('color', 'stat', 'variable_one', 'variable_two', 'variable_three',)


class CowboyHatForm(forms.ModelForm):
    """
    Form for designing custom sunglasses
    """
    animal = [
        ('Animal - Horse', "Horse"),
        ('Animal - Cow', "Cow"),
        ('Animal - Giraffe', "Giraffe"),
    ]

    weapon = [
        ('Weapon - Six Shooter', "Six Shooter"),
        ('Weapon - Knife', "Knife"),
        ('Weapon - Sword', "Sword"),
    ]

    musical_instrument = [
        ('Instrument - Trumpet', "Trumpet"),
        ('Instrument - Saxophone', "Saxophone"),
        ('Instrument - Toooooooba', "Toooooooba"),
        ('Instrument - None', "None"),
    ]

    variable_one = forms.ChoiceField(choices=animal, label="Animal")
    variable_two = forms.ChoiceField(choices=weapon, label="Weapon")
    variable_three = forms.ChoiceField(choices=musical_instrument, label="Musical Instrument")

    class Meta:
        model = Product
        fields = ('color', 'stat', 'variable_one', 'variable_two', 'variable_three',)


class SatinHatForm(forms.ModelForm):
    """
    Form for designing a custom hat.
    """
    brim_width = [
        ('Brim - 20cm', "20cm"),
        ('Brim - 25cm', "25cm"),
        ('Brim - 30cm', "30cm"),
    ]

    hat_material = [
        ('Material - Satin', "Satin"),
        ('Material - Felt', "Felt"),
        ('Material - Scratchy Wool', "Scratchy Wool"),
    ]

    pattern = [
        ('Pattern - Floral', "Floral"),
        ('Pattern - Mushrooms', "Mushrooms with Faces"),
        ('Pattern - Sixties', "60s Repeating Pattern"),
        ('Pattern - None', "None"),
    ]

    variable_one = forms.ChoiceField(choices=brim_width, label="Brim Width")
    variable_two = forms.ChoiceField(choices=hat_material, label="Hat Material")
    variable_three = forms.ChoiceField(choices=pattern, label="Pattern")

    class Meta:
        model = Product
        fields = ('color', 'stat', 'variable_one', 'variable_two', 'variable_three',)
