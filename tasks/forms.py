from django.forms import ModelForm

from .models import Pilot


class PilotForm(ModelForm):
    class Meta:
        model = Pilot
        fields = ['title', 'name', 'acronym', 'team', 'track']
