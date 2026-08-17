from django import forms 


SELECT_CLASS = (
    "block w-full rounded-md border-gray-300 shadow-sm "
    "focus:border-indigo-500 focus:ring "
    "focus:ring-indigo-200 focus:ring-opacity-50"
)

class DeckCreationForm(forms.Form):

    name = forms.CharField(
        required=True,
        label="Deck Name",
        widget=forms.TextInput(
            attrs={
                'class': SELECT_CLASS,
                'placeholder': 'Enter deck name...'
            }
        )

    format = forms.ChoiceField(
        choices=[
            ('', 'All Set Names'),
            ('standard', 'Standard'),
            ('commander', 'commander'),
        ],
        required=False,
        widget=forms.Select(attrs={'class': SELECT_CLASS})
    )

    private = forms.BooleanField(
        required=True,
        label="Make this private",
        widget=forms.CheckboxInput(attrs={
            'class': 'rounded h-4 w-4'
        })
    )