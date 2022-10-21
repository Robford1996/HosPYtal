from django.forms import ModelForm
from .models import Checkins


class CheckinsForm(ModelForm):
    class Meta:
        model = Checkins
        fields = ['date', 'time', 'notes']
