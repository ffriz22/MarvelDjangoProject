from django.forms import ModelForm

from applicationMarvel.models import Creator, Character, Comic, Event, Story


class CreatorForm(ModelForm):
    class Meta:
        model = Creator
        exclude = ('user', )


class CharacterForm(ModelForm):
    class Meta:
        model = Character
        exclude = ('user', )


class ComicForm(ModelForm):
    class Meta:
        model = Comic
        exclude = ('user', )


class EventForm(ModelForm):
    class Meta:
        model = Event
        exclude = ('user', )


class StoryForm(ModelForm):
    class Meta:
        model = Story
        exclude = ('user', )