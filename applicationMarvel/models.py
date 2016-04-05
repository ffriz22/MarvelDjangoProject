from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from datetime import date


class Creator(models.Model):
    firstName = models.TextField(max_length=100, null=True) #The first name of the creator.,
    middleName = models.TextField(max_length=100, null=True, blank=True) #The middle name of the creator.,
    lastName = models.TextField(max_length=100, null=True) #The last name of the creator.,
    suffix = models.TextField(max_length=100, null=True) #The suffix or honorific for the creator.,
    fullName = models.TextField(max_length=100) #The full name of the creator (a space-separated concatenation of the above four fields).,
    modified = models.DateField() #The date the resource was most recently modified.,
    resourceURI = models.TextField(max_length=100) #The canonical URL identifier for this resource.,
    thumbnail = models.ImageField(upload_to="applicationMarvel", blank=True, null=True) #The representative image for this creator.,

    def __unicode__(self):
        return u"%s" % self.fullName
    def get_absolute_url(self):
        return reverse_lazy('applicationMarvel:creator_detail', kwargs={'pk': self.pk})
#end of Creator model


class Story(models.Model):
    title = models.TextField(max_length=100)# The story title.,
    description = models.TextField(max_length=100, null=True)# A short description of the story.,
    resourceURI = models.TextField(max_length=100)# The canonical URL identifier for this resource. ,
    type  = models.TextField(max_length=100, null=True)# The story type e.g. interior story, cover, text story.,
    modified = models.DateField()# The date the resource was most recently modified.,
    thumbnail = models.ImageField(upload_to="applicationMarvel", blank=True, null=True) # The representative image for this story.,
    creator = models.ForeignKey(Creator)

    def __unicode__(self):
        return u"%s" % self.title

    def get_absolute_url(self):
        return reverse_lazy('applicationMarvel:story_detail', kwargs={'pk': self.pk})
#End of Story Model


class Comic(models.Model):
    title = models.TextField(max_length=100) #The canonical title of the comic.,
    description = models.TextField(max_length=100, null=True) #The preferred description of the comic.,
    modified = models.DateField() #The date the resource was most recently modified.,
    isbn = models.TextField(max_length=100) #The ISBN for the comic (generally only populated for collection formats).,,
    pageCount = models.IntegerField() #The number of story pages in the comic.,
    resourceURI = models.TextField(max_length=100) #The canonical URL identifier for this resource.,
    price = models.FloatField() #prices for this comic
    thumbnail = models.ImageField(upload_to="applicationMarvel", blank=True, null=True) #The representative image for this comic.,
    images = models.CommaSeparatedIntegerField(max_length=100) #A list of promotional images associated with this comic.,
    creator = models.ForeignKey(Creator)
    stories = models.ForeignKey(Story)

    def __unicode__(self):
        return u"%s" % self.title

    def get_absolute_url(self):
        return reverse_lazy('applicationMarvel:comic_detail', kwargs={'pk': self.pk})
#end of comic module


class Character(models.Model):
    name = models.TextField(max_length=100) #The name of the character.,
    description = models.TextField(max_length=100, null=True) #A short bio or description of the character.,
    modified = models.DateField() #The date the resource was most recently modified.,
    resourceURI = models.TextField(max_length=100) #The canonical URL identifier for this resource.,
    thumbnail = models.ImageField(upload_to="applicationMarvel", blank=True, null=True) #The representative image for this character.,
    comics = models.ForeignKey(Comic)
    stories = models.ForeignKey(Story)
    creator = models.ForeignKey(Creator) #A resource list containing the creators associated with this comic.,

    def __unicode__(self):
        return u"%s" % self.name

    def get_absolute_url(self):
        return reverse_lazy('applicationMarvel:character_detail', kwargs={'pk': self.pk})
#end of characters model


class Event(models.Model):
    title = models.TextField(max_length=100) #The title of the event.,
    description = models.TextField(max_length=100, null=True) #A description of the event.,
    resourceURI = models.TextField(max_length=100) #The canonical URL identifier for this resource.,
    modified = models.DateField() #The date the resource was most recently modified.,
    start = models.DateField() #The date of publication of the first issue in this event.,
    end = models.DateField() #The date of publication of the last issue in this event.,
    thumbnail = models.ImageField(upload_to="applicationMarvel", blank=True, null=True) #The representative image for this event.,
    comics = models.ForeignKey(Comic)
    stories = models.ForeignKey(Story)
    creator = models.ForeignKey(Creator)
    character = models.ForeignKey(Character)

    def __unicode__(self):
        return u"%s" % self.title

    def get_absolute_url(self):
        return reverse_lazy('applicationMarvel:event_detail', kwargs={'pk': self.pk})
#end of event module
#http://developer.marvel.com/docs#!/public/getCreatorCollection_get_0
# Create your models here.
