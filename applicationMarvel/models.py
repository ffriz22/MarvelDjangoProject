from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from datetime import date

class Image (models.Model):
    id = models.IntegerField(primary_key=True)
    path = models.TextField(max_length=100) #The directory path of to the image.,
    extension = models.TextField(max_length=100) #The file extension for the image.

    def __unicode__(self):
        return u"%s" % (self.path + "." + self.extension)
#end of Image model


class Creator(models.Model):
    id = models.IntegerField(primary_key=True) #The unique ID of the creator resource.,
    firstName = models.TextField(max_length=100, null=True) #The first name of the creator.,
    middleName = models.TextField(max_length=100, null=True) #The middle name of the creator.,
    lastName = models.TextField(max_length=100, null=True) #The last name of the creator.,
    suffix = models.TextField(max_length=100, null=True) #The suffix or honorific for the creator.,
    fullName = models.TextField(max_length=100) #The full name of the creator (a space-separated concatenation of the above four fields).,
    modified = models.DateField() #The date the resource was most recently modified.,
    resourceURI = models.TextField(max_length=100) #The canonical URL identifier for this resource.,
    thumbnail = models.ForeignKey(Image, null=True) #The representative image for this creator.,
    stories = models.CommaSeparatedIntegerField(max_length=100) #A resource list containing the stories which feature work by this creator.,
    comics = models.CommaSeparatedIntegerField(max_length=100) #A resource list containing the comics which feature work by this creator.,
    events = models.CommaSeparatedIntegerField(max_length=100) #A resource list containing the events which feature work by this creator.

    def __unicode__(self):
        return u"%s" % self.fullName
    def get_absolute_url(self):
        return reverse('applicationMarvel:creator_detail', kwargs={'pk': self.pk})
#end of Creator model


class Story(models.Model):
    id = models.IntegerField(primary_key=True) # The unique ID of the story resource.,
    title = models.TextField(max_length=100)# The story title.,
    description = models.TextField(max_length=100, null=True)# A short description of the story.,
    resourceURI = models.TextField(max_length=100)# The canonical URL identifier for this resource. ,
    type  = models.TextField(max_length=100, null=True)# The story type e.g. interior story, cover, text story.,
    modified = models.DateField()# The date the resource was most recently modified.,
    thumbnail = models.ForeignKey(Image, null=True)# The representative image for this story.,
    comics = models.CommaSeparatedIntegerField(max_length=100)# A resource list containing comics in which this story takes place.,
    events = models.CommaSeparatedIntegerField(max_length=100)# A resource list of the events in which this story appears.,
    characters = models.CommaSeparatedIntegerField(max_length=100)# A resource list of characters which appear in this story.,
    creators = models.CommaSeparatedIntegerField(max_length=100)# A resource list of creators who worked on this story.,

    def __unicode__(self):
        return u"%s" % self.fullName

    def get_absolute_url(self):
        return reverse('applicationMarvel:story_detail', kwargs={'pk': self.pk})
#End of Story Model


class Event(models.Model):
    id = models.IntegerField(primary_key=True) #The unique ID of the event resource.,
    title = models.TextField(max_length=100) #The title of the event.,
    description = models.TextField(max_length=100, null=True) #A description of the event.,
    resourceURI = models.TextField(max_length=100) #The canonical URL identifier for this resource.,
    modified = models.DateField() #The date the resource was most recently modified.,
    start = models.DateField() #The date of publication of the first issue in this event.,
    end = models.DateField() #The date of publication of the last issue in this event.,
    thumbnail = models.ForeignKey(Image, null=True) #The representative image for this event.,
    comics = models.CommaSeparatedIntegerField(max_length=100) #A resource list containing the comics in this event.,
    stories = models.CommaSeparatedIntegerField(max_length=100) #A resource list containing the stories in this event.,
    characters = models.CommaSeparatedIntegerField(max_length=100) #A resource list containing the characters which appear in this event.,
    creators = models.CommaSeparatedIntegerField(max_length=100) #A resource list containing creators whose work appears in this event.,
    #next = models.ForeignKey(Event) #A summary representation of the event which follows this event.,
    #previous = models.ForeignKey(Event) #A summary representation of the event which preceded this event.

    def __unicode__(self):
        return u"%s" % self.title

    def get_absolute_url(self):
        return reverse('applicationMarvel:event_detail', kwargs={'pk': self.pk})
#end of event module


class Comic(models.Model):
    id = models.IntegerField(primary_key=True) #The unique ID of the comic resource.,
    title = models.TextField(max_length=100) #The canonical title of the comic.,
    description = models.TextField(max_length=100, null=True) #The preferred description of the comic.,
    modified = models.DateField() #The date the resource was most recently modified.,
    isbn = models.TextField(max_length=100) #The ISBN for the comic (generally only populated for collection formats).,,
    pageCount = models.IntegerField() #The number of story pages in the comic.,
    resourceURI = models.TextField(max_length=100) #The canonical URL identifier for this resource.,
    price = models.FloatField() #prices for this comic
    thumbnail = models.ForeignKey(Image, null=True) #The representative image for this comic.,
    images = models.CommaSeparatedIntegerField(max_length=100) #A list of promotional images associated with this comic.,
    creators = models.CommaSeparatedIntegerField(max_length=100) #A resource list containing the creators associated with this comic.,
    characters = models.CommaSeparatedIntegerField(max_length=100) #A resource list containing the characters which appear in this comic.,
    stories = models.CommaSeparatedIntegerField(max_length=100) #A resource list containing the stories which appear in this comic.,
    events = models.CommaSeparatedIntegerField(max_length=100) #A resource list containing the events in which this comic appears.

    def __unicode__(self):
        return u"%s" % self.title

    def get_absolute_url(self):
        return reverse('applicationMarvel:comic_detail', kwargs={'pk': self.pk})
#end of comic module


class Character(models.Model):
    id = models.IntegerField(primary_key=True) #The unique ID of the character resource.,
    name = models.TextField(max_length=100) #The name of the character.,
    description = models.TextField(max_length=100, null=True) #A short bio or description of the character.,
    modified = models.DateField() #The date the resource was most recently modified.,
    resourceURI = models.TextField(max_length=100) #The canonical URL identifier for this resource.,
    thumbnail = models.ForeignKey(Image, null=True) #The representative image for this character.,
    comics = models.CommaSeparatedIntegerField(max_length=100) #A resource list containing comics which feature this character.,
    stories= models.CommaSeparatedIntegerField(max_length=100) #A resource list of stories in which this character appears.,
    events = models.CommaSeparatedIntegerField(max_length=100) #A resource list of events in which this character appears.,
    creator = models.ForeignKey(Creator) #A resource list containing the creators associated with this comic.,

    def __unicode__(self):
        return u"%s" % self.name

    def get_absolute_url(self):
        return reverse('applicationMarvel:character_detail', kwargs={'pk': self.pk})
#end of characters model

#http://developer.marvel.com/docs#!/public/getCreatorCollection_get_0
# Create your models here.
