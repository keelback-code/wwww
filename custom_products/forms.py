from django import forms
from .models import CustomProduct


class CustomProductForm(forms.ModelForm):
    """
    Form for designing a custom hat.
    """
    class Meta:
        model = CustomProduct
        fields = '__all__'