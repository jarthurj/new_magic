from django import forms
from .models import UserDeck

SELECT_CLASS = (
    "block w-full rounded-md border-gray-300 shadow-sm "
    "focus:border-indigo-500 focus:ring "
    "focus:ring-indigo-200 focus:ring-opacity-50"
)

INPUT_CLASS = (
    "block w-full rounded-md border-gray-300 shadow-sm "
    "focus:border-indigo-500 focus:ring "
    "focus:ring-indigo-200 focus:ring-opacity-50"
)

CHECKBOX_CLASS = "rounded border-gray-300 text-indigo-600"

class DeckCreationForm(forms.ModelForm):
    class Meta:
        model = UserDeck
        fields = ['name', 'format', 'private']
        widgets = {
            'name': forms.TextInput(attrs={'class': INPUT_CLASS}),
            'format': forms.Select(attrs={'class': SELECT_CLASS}),
            'private': forms.CheckboxInput(attrs={'class': CHECKBOX_CLASS}),
        }