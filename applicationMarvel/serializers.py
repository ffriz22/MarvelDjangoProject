from rest_framework.fields import CharField
from rest_framework.relations import HyperlinkedRelatedField, HyperlinkedIdentityField
from rest_framework.serializers import HyperlinkedModelSerializer
from models import Creator, Story, Comic, Character, Event

class CreatorSerializer(HyperlinkedModelSerializer):
    uri = HyperlinkedIdentityField(view_name='applicationMarvel:creator_detail')
    story_set = HyperlinkedRelatedField(many=True, read_only=True, view_name='applicationMarvel:story_detail')
    comic_set = HyperlinkedRelatedField(many=True, read_only=True, view_name='applicationMarvel:comic_detail')
    character_set = HyperlinkedRelatedField(many=True, read_only=True,
                                            view_name='applicationMarvel:character_detail')
    event_set = HyperlinkedRelatedField(many=True, read_only=True, view_name='applicationMarvel:event_detail')
    user = CharField(read_only=True)
    class Meta:
        model = Creator
        fields = ('uri', 'firstName', 'middleName', 'lastName', 'suffix', 'fullName', 'modified', 'resourceURI', 'thumbnail',
                  'story_set', 'comic_set', 'character_set', 'event_set', 'user')

class StorySerializer(HyperlinkedModelSerializer):
    uri = HyperlinkedIdentityField(view_name='applicationMarvel:story_detail')
    creator = HyperlinkedRelatedField(many=False, read_only=True, view_name='applicationMarvel:creator_detail')
    comic_set = HyperlinkedRelatedField(many=True, read_only=True, view_name='applicationMarvel:comic_detail')
    character_set = HyperlinkedRelatedField(many=True, read_only=True,
                                            view_name='applicationMarvel:character_detail')
    event_set = HyperlinkedRelatedField(many=True, read_only=True, view_name='applicationMarvel:event_detail')
    user = CharField(read_only=True)
    class Meta:
        model = Story
        fields = ('uri', 'title', 'description', 'resourceURI', 'type', 'modified', 'thumbnail', 'creator',
                  'comic_set', 'character_set', 'event_set', 'user')

class ComicSerializer(HyperlinkedModelSerializer):
    uri = HyperlinkedIdentityField(view_name='applicationMarvel:comic_detail')
    creator = HyperlinkedRelatedField(many=False, read_only=True, view_name='applicationMarvel:creator_detail')
    stories = HyperlinkedRelatedField(many=False, read_only=True, view_name='applicationMarvel:story_detail')
    character_set = HyperlinkedRelatedField(many=True, read_only=True,
                                            view_name='applicationMarvel:character_detail')
    event_set = HyperlinkedRelatedField(many=True, read_only=True, view_name='applicationMarvel:event_detail')
    user = CharField(read_only=True)
    class Meta:
        model = Comic
        fields = ('uri', 'title', 'description', 'modified', 'isbn', 'pageCount', 'resourceURI', 'price', 'thumbnail',
                  'creator', 'stories', 'character_set', 'event_set', 'user')

class CharacterSerializer(HyperlinkedModelSerializer):
    uri = HyperlinkedIdentityField(view_name='applicationMarvel:character_detail')
    creator = HyperlinkedRelatedField(many=False, read_only=True, view_name='applicationMarvel:creator_detail')
    stories = HyperlinkedRelatedField(many=False, read_only=True, view_name='applicationMarvel:story_detail')
    comics = HyperlinkedRelatedField(many=False, read_only=True, view_name='applicationMarvel:comic_detail')
    event_set = HyperlinkedRelatedField(many=True, read_only=True, view_name='applicationMarvel:event_detail')
    user = CharField(read_only=True)
    class Meta:
        model = Character
        fields = ('uri', 'name', 'description', 'modified', 'resourceURI', 'thumbnail', 'creator', 'comics', 'stories',
                  'event_set', 'user')

class EventSerializer(HyperlinkedModelSerializer):
    uri = HyperlinkedIdentityField(view_name='applicationMarvel:event_detail')
    creator = HyperlinkedRelatedField(many=False, read_only=True, view_name='applicationMarvel:creator_detail')
    stories = HyperlinkedRelatedField(many=False, read_only=True, view_name='applicationMarvel:story_detail')
    comics = HyperlinkedRelatedField(many=False, read_only=True, view_name='applicationMarvel:comic_detail')
    user = CharField(read_only=True)
    class Meta:
        model = Event
        fields = ('uri', 'title', 'description', 'resourceURI', 'modified', 'start', 'end', 'thumbnail', 'comics',
                  'stories', 'creator', 'user')