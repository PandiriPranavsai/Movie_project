from django import forms


from .models import *


# form which is used for the model Movie

class MovieForm(forms.ModelForm):
      class Meta:
        model=Movie
        fields='__all__'