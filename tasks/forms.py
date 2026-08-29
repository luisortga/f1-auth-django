from django import forms

from .models import Pilot


class PilotForm(forms.ModelForm):
    class Meta:
        model = Pilot
        fields = ['title', 'name', 'acronym', 'team', 'track']
        widgets = {
            'title': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Write a title'}
            ),
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Write the name of the pilot',
                }
            ),
            'acronym': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'VER'}
            ),
            'team': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Write the team'}
            ),
            'track': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Write the track'}
            ),
        }
