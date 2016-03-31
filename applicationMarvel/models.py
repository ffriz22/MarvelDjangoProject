from __future__ import unicode_literals
from django.db import models


class Image:
    path = models.TextField() #The directory path of to the image.,
    extension = models.TextField() #The file extension for the image.
#end of Image model

"""

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
"""



class Comic:
    id = models.IntegerField() #The unique ID of the comic resource.,
    title = models.TextField() #The canonical title of the comic.,
    description = models.TextField() #The preferred description of the comic.,
    modified = models.DateField() #The date the resource was most recently modified.,
    isbn = models.TextField() #The ISBN for the comic (generally only populated for collection formats).,,
    pageCount = models.IntegerField() #The number of story pages in the comic.,
    resourceURI = models.TextField() #The canonical URL identifier for this resource.,
    price = models.FloatField() #prices for this comic
    thumbnail = models.ForeignKey(Image) #The representative image for this comic.,
    images = models.CommaSeparatedIntegerField() #A list of promotional images associated with this comic.,
    creators = models.CommaSeparatedIntegerField() #A resource list containing the creators associated with this comic.,
    characters = models.CommaSeparatedIntegerField() #A resource list containing the characters which appear in this comic.,
    stories = models.CommaSeparatedIntegerField() #A resource list containing the stories which appear in this comic.,
    events = models.CommaSeparatedIntegerField() #A resource list containing the events in which this comic appears.
#end of comic module

#falte creadors

class Character(models.Model):
    id = models.IntegerField() #The unique ID of the character resource.,
    name = models.TextField() #The name of the character.,
    description = models.TextField() #A short bio or description of the character.,
    modified = models.DateField() #The date the resource was most recently modified.,
    resourceURI = models.TextField() #The canonical URL identifier for this resource.,
    thumbnail = models.ForeignKey(Image) #The representative image for this character.,
    comics = models.CommaSeparatedIntegerField() #A resource list containing comics which feature this character.,
    stories= models.CommaSeparatedIntegerField() #A resource list of stories in which this character appears.,
    events = models.CommaSeparatedIntegerField() #A resource list of events in which this character appears.,
    creator = models.ForeignKey(Creator) #A resource list containing the creators associated with this comic.,
#end of characters model

#http://developer.marvel.com/docs#!/public/getCreatorCollection_get_0
# Create your models here.
