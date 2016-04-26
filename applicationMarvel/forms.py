from django.forms import ModelForm

from applicationMarvel.models import Creator


class CreatorForm(ModelForm):
    class Meta:
        model = Creator
        exclude = ('user', )