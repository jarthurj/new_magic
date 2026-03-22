from django import forms 
from .models import (SetId,SetCode,SetName,Rarity,Color,
                    ColorIdentity,Keywords,ManaCostColor,Type,ReleasedAt,
                    Name,Card)

class SetCodeForm(forms.ModelForm):

    set_code = forms.ModelChoiceField(
        queryset=SetCode.objects.all(),           # all SetId objects
        empty_label="Select Set Code",            # placeholder option
        to_field_name="set_code",                     # use set_id value instead of object ID
        widget=forms.Select(
            attrs={
                'class': 'block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring focus:ring-indigo-200 focus:ring-opacity-50'
            }
        )
    )
    class Meta:
        model = SetCode
        fields = ['set_code']