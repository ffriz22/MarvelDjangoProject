from rest_framework.fields import CharField
from rest_framework.relations import HyperlinkedRelatedField, HyperlinkedIdentityField
from rest_framework.serializers import HyperlinkedModelSerializer
from models import Creator, Story, Comic, Character, Event

class CreatorSerializer(HyperlinkedModelSerializer):
    uri = HyperlinkedIdentityField(view_name='applicationMarvel:creator_detail.html')
    story_set = HyperlinkedRelatedField(many=True, read_only=True, view_name='applicationMarvel:story_detail.html')
    comic_set = HyperlinkedRelatedField(many=True, read_only=True, view_name='applicationMarvel:comic_detail.html')
    character_set = HyperlinkedRelatedField(many=True, read_only=True,
                                            view_name='applicationMarvel:character_detail.html')
    event_set = HyperlinkedRelatedField(many=True, read_only=True, view_name='applicationMarvel:event_detail.html')
    user = CharField(read_only=True)
    class Meta:
        model = Creator
        fields = ('firstName', 'middleName', 'lastName', 'suffix', 'fullName', 'modified', 'resourceURI', 'thumbnail',
                  'story_set', 'comic_set', 'character_set', 'event_set', 'user')

class StorySerializer(HyperlinkedModelSerializer):
    uri = HyperlinkedIdentityField(view_name='applicationMarvel:story_detail.html')
    creator = HyperlinkedRelatedField(view_name='applicationMarvel:creator_detail.html')
    comic_set = HyperlinkedRelatedField(many=True, read_only=True, view_name='applicationMarvel:comic_detail.html')
    character_set = HyperlinkedRelatedField(many=True, read_only=True,
                                            view_name='applicationMarvel:character_detail.html')
    event_set = HyperlinkedRelatedField(many=True, read_only=True, view_name='applicationMarvel:event_detail.html')
    user = CharField(read_only=True)
    class Meta:
        model = Story
        fields = ('title', 'description', 'resourceURI', 'type', 'modified', 'thumbnail', 'creator',
                  'comic_set', 'character_set', 'event_set', 'user')

class ComicSerializer(HyperlinkedModelSerializer):
    uri = HyperlinkedIdentityField(view_name='applicationMarvel:comic_detail.html')
    creator = HyperlinkedRelatedField(view_name='applicationMarvel:creator_detail.html')
    story = HyperlinkedRelatedField(view_name='applicationMarvel:story_detail.html')
    character_set = HyperlinkedRelatedField(many=True, read_only=True,
                                            view_name='applicationMarvel:character_detail.html')
    event_set = HyperlinkedRelatedField(many=True, read_only=True, view_name='applicationMarvel:event_detail.html')
    user = CharField(read_only=True)
    class Meta:
        model = Comic
        fields = ('title', 'description', 'modified', 'isbn', 'pageCount', 'resourceURI', 'price', 'thumbnail',
                  'creator', 'stories', 'character_set', 'event_set' 'user')

class CharacterSerializer(HyperlinkedModelSerializer):
    uri = HyperlinkedIdentityField(view_name='applicationMarvel:character_detail.html')
    creator = HyperlinkedRelatedField(view_name='applicationMarvel:creator_detail.html')
    story = HyperlinkedRelatedField(view_name='applicationMarvel:story_detail.html')
    comic = HyperlinkedRelatedField(view_name='applicationMarvel:comic_detail.html')
    event_set = HyperlinkedRelatedField(many=True, read_only=True, view_name='applicationMarvel:event_detail.html')
    user = CharField(read_only=True)
    class Meta:
        model = Character
        fields = ('name', 'description', 'modified', 'resourceURI', 'thumbnail', 'creator', 'comics', 'stories',
                  'event_set,' 'user')

class EventSerializer(HyperlinkedModelSerializer):
    uri = HyperlinkedIdentityField(view_name='applicationMarvel:event_detail.html')
    creator = HyperlinkedRelatedField(view_name='applicationMarvel:creator_detail.html')
    story = HyperlinkedRelatedField(view_name='applicationMarvel:story_detail.html')
    comic = HyperlinkedRelatedField(view_name='applicationMarvel:comic_detail.html')
    event = HyperlinkedRelatedField(view_name='applicationMarvel:event_detail.html')
    user = CharField(read_only=True)
    class Meta:
        model = Event
        fields = ('title', 'description', 'resourceURI', 'modified', 'start', 'end', 'thumbnail', 'comics',
                  'stories', 'creator', 'character', 'user')