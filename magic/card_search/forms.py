from django import forms 
from .models import (SetId,SetCode,SetName,Rarity,Color,
                    ColorIdentity,Keywords,ManaCostColor,Type,ReleasedAt,
                    Name,Card)

SELECT_CLASS = (
    "block w-full rounded-md border-gray-300 shadow-sm "
    "focus:border-indigo-500 focus:ring "
    "focus:ring-indigo-200 focus:ring-opacity-50"
)

class CardSearchForm(forms.Form):




    set_name = forms.ModelChoiceField(
        queryset=SetName.objects.order_by('set_name'),
        required=False,
        empty_label="All Set Names",
        widget=forms.Select(
            attrs={'class': SELECT_CLASS}
        )
    )

    rarity = forms.ModelChoiceField(
        queryset=Rarity.objects.all(),
        required=False,
        empty_label="All Rarity",
        widget=forms.Select(
            attrs={'class': SELECT_CLASS}
        )
    )

    name = forms.CharField(
        required=False,
        label="Name Search",
        widget=forms.TextInput(
            attrs={
                'class': SELECT_CLASS,
                'placeholder': 'Enter card name...'
            }
        )
    )
    type = forms.ModelChoiceField(
        queryset=Type.objects.order_by('type'),
        required=False,
        empty_label="All Types",
        widget=forms.Select(
            attrs={'class': SELECT_CLASS}
        )
    )

    cmc = forms.ModelChoiceField(
        queryset=Card.objects
            .values_list('cmc', flat=True)
            .distinct()
            .order_by('cmc'),
        required=False,
        empty_label="Converted Mana Cost",
        widget=forms.Select(
            attrs={'class': SELECT_CLASS}
        )
    )
# rarity
# name
# colors
# keywords
# type

    # class Meta:
    #     model = SetName
    #     fields = ['set_name','rarity']