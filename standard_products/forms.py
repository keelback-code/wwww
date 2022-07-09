from django import forms
from .models import StandardProduct, Stat


class StandardProductForm(forms.ModelForm):
    """
    Form for dealing with standard products.
    Based on Code Institute Boutique Ado project.
    """
    class Meta:
        model = StandardProduct
        fields = '__all__'
    
    image = forms.ImageField(label='Image', required=False)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # stats = Stat.objects.all()
        # friendly_names = [(s.id, s.get_friendly_name()) for s in stats]

        # self.fields['stat_one', 'stat_two',].choices = friendly_names
        # for field_name, field in self.fields.items():
        #     field.widget.attrs['class'] = 'border-black rounded-0'
