from __future__ import unicode_literals
from django.db import models


class Image:
    path = models.TextField() #The directory path of to the image.,
    extension = models.TextField() #The file extension for the image.
#end of Image model


class ComicList:
    available = models.IntegerField() #The number of total available issues in this list. Will always be greater than or equal to the "returned" value.,
    returned = models.IntegerField() #The number of issues returned in this collection (up to 20).,
    collectionURI = models.TextField() #The path to the full list of issues in this collection.,
    items = models.TextField() #The list of returned issues in this collection.
#end of ComicList model


class StoryList:
    available = models.IntegerField() #The number of total available stories in this list. Will always be greater than or equal to the "returned" value.,
    returned = models.IntegerField() #The number of stories returned in this collection (up to 20).,
    collectionURI = models.TextField() #The path to the full list of stories in this collection.,
    items = models.TextField() #The list of returned stories in this collection.
#end of StoryList model


class EventList:
    available = models.IntegerField() #The number of total available events in this list. Will always be greater than or equal to the "returned" value.,
    returned = models.IntegerField() #The number of events returned in this collection (up to 20).,
    collectionURI = models.TextField() #The path to the full list of events in this collection.,
    items = models.TextField() #The list of returned events in this collection.
#end of EventList model


class SeriesList:
    available = models.IntegerField() #The number of total available series in this list. Will always be greater than or equal to the "returned" value.,
    returned = models.IntegerField() #The number of series returned in this collection (up to 20).,
    collectionURI = models.TextField() #The path to the full list of series in this collection.,
    items = models.TextField() #The list of returned series in this collection.
#end of SeriesList model


class Characters(models.Model):
    id = models.IntegerField() #The unique ID of the character resource.,
    name = models.TextField() #The name of the character.,
    description = models.TextField() #A short bio or description of the character.,
    modified = models.DateField() #The date the resource was most recently modified.,
    resourceURI = models.TextField() #The canonical URL identifier for this resource.,
    url = models.URLField #(sol usem una) A set of public web site URLs for the resource.,
    thumbnail = Image() #The representative image for this character.,
    comics = models.ForeignKey(ComicList) #A resource list containing comics which feature this character.,
    stories = models.ForeignKey(StoryList) #A resource list of stories in which this character appears.,
    events = models.ForeignKey(EventList) #A resource list of events in which this character appears.,
    series = models.ForeignKey(SeriesList) #A resource list of series in which this character appears.
#end of characters model

#http://developer.marvel.com/docs#!/public/getCreatorCollection_get_0
# Create your models here.
