# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from django.core.urlresolvers import reverse_lazy
from django.views.generic import RedirectView

from models import Creator
from views import CreatorDetail, CreatorList, ComicDetail, ComicList, StoryDetail, StoryList, EventDetail, EventList, CharacterDetail, CharacterList

urlpatterns = patterns('',
    # Home page
    url(r'^$',
        RedirectView.as_view(url=reverse_lazy('applicationMarvel:creator_list', kwargs={'extension': 'html'})),
        name='home'),

    # List creators: /applicationMarvel/creator.json
    url(r'^creators\.(?P<extension>(json|xml|html))$',
        CreatorList.as_view(),
        name='creator_list'),

    # Creator details, ex.: /applicationMarvel/creator/1.json
    url(r'^creator/(?P<pk>\d+)\.(?P<extension>(json|xml|html))$',
        CreatorDetail.as_view(),
        name='creator_detail'),

    # List comics: /applicationMarvel/comics.json
    url(r'^comics\.(?P<extension>(json|xml|html))$',
        ComicList.as_view(),
        name='comic_list'),

    # Comic details, ex.: /applicationMarvel/comic/1.json
    url(r'^comic/(?P<pk>\d+)\.(?P<extension>(json|xml|html))$',
       ComicDetail.as_view(),
       name='comic_detail'),

    # List stories /applicationMarvel/stories.json
    url(r'^stories\.(?P<extension>(json|xml|html))$',
        StoryList.as_view(),
        name='stories_list'),

    # Story details, ex.: /applicationMarvel/story/1.json
    url(r'^story/(?P<pk>\d+)\.(?P<extension>(json|xml|html))$',
       StoryDetail.as_view(),
       name='story_detail'),

    # List events /applicationMarvel/events.json
    url(r'^events\.(?P<extension>(json|xml|html))$',
       EventList.as_view(),
       name='events_list'),

    # Event details, ex.: /applicationMarvel/event/1.json
    url(r'^event/(?P<pk>\d+)\.(?P<extension>(json|xml|html))$',
       EventDetail.as_view(),
       name='event_detail'),

    # List characters /applicationMarvel/characters.json
    url(r'characters\.(?P<extension>(json|xml|html))$',
        CharacterList.as_view(),
       name='characters_list'),

    # Character details, ex.: /applicationMarvel/character/1.json
    url(r'^character/(?P<pk>\d+)\.(?P<extension>(json|xml|html))$',
       CharacterDetail.as_view(),
       name='character_detail'),
)