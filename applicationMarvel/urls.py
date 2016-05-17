# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from django.core.urlresolvers import reverse_lazy
from django.views.generic import RedirectView, UpdateView

from forms import CreatorForm, CharacterForm, ComicForm, EventForm, StoryForm
from models import Creator, Character, Comic, Event, Story
from views import CreatorDetail, CreatorList, ComicDetail, ComicList, StoryDetail, StoryList, EventDetail, EventList, \
    CharacterDetail, CharacterList, CharacterCreate, ComicCreate, CreatorCreate, EventCreate, StoryCreate, \
    CreatorDelete, ComicDelete, CharacterDelete, StoryDelete, EventDelete, APICreatorDetail, APICreatorList, \
    APIStoryDetail, APIStoryList, APIComicDetail, APIComicList, APICharacterDetail, APICharacterList, \
    APIEventDetail, APIEventList,


urlpatterns = patterns('',
                       # Home page
                       url(r'^$',
                           RedirectView.as_view(url=reverse_lazy('applicationMarvel:creator_list')),
                           name='home'),

                       # List creators: /applicationMarvel/creator.json
                       url(r'^creators(\.(?P<extension>(json|xml)))?$',
                           CreatorList.as_view(),
                           name='creator_list'),

                       # Creator details, ex.: /applicationMarvel/creator/1.json
                       url(r'^creator/(?P<pk>\d+)(\.(?P<extension>(json|xml)))?$',
                           CreatorDetail.as_view(),
                           name='creator_detail'),

                       # Edit creator details, ex.: applicationMarvel/creator/1/edit/
                       url(r'^creator/(?P<pk>\d+)/edit/$',
                           UpdateView.as_view(
                               model=Creator,
                               template_name='applicationMarvel/formularis/form.html',
                               form_class=CreatorForm),
                           name='creator_edit'),

                       # Create a creator /applicationMarvel/creators/create/
                       url(r'^creators/create/$',
                           CreatorCreate.as_view(),
                           name='creator_create'),

                       # Delete creator details, ex.: applicationMarvel/creator/1/delete/
                       url(r'^creator/(?P<pk>\d+)/delete/$',
                           CreatorDelete.as_view(),
                           name='creator_delete'),

                       # List comics: /applicationMarvel/comics.json
                       url(r'^comics(\.(?P<extension>(json|xml)))?$',
                           ComicList.as_view(),
                           name='comic_list'),

                       # Comic details, ex.: /applicationMarvel/comic/1.json
                       url(r'^comic/(?P<pk>\d+)(\.(?P<extension>(json|xml)))?$',
                           ComicDetail.as_view(),
                           name='comic_detail'),

                       # Edit comic details, ex.: applicationMarvel/comic/1/edit/
                       url(r'^comic/(?P<pk>\d+)/edit/$',
                           UpdateView.as_view(
                               model=Comic,
                               template_name='applicationMarvel/formularis/form.html',
                               form_class=ComicForm),
                           name='comic_edit'),

                       # Create a comic /applicationMarvel/comics/create/
                       url(r'^comics/create/$',
                           ComicCreate.as_view(),
                           name='comic_create'),

                       # Delete comic details, ex.: applicationMarvel/comic/1/delete/
                       url(r'^comic/(?P<pk>\d+)/delete/$',
                           ComicDelete.as_view(),
                           name='comic_delete'),

                       # List stories /applicationMarvel/stories.json
                       url(r'^stories(\.(?P<extension>(json|xml)))?$',
                           StoryList.as_view(),
                           name='stories_list'),

                       # Story details, ex.: /applicationMarvel/story/1.json
                       url(r'^story/(?P<pk>\d+)(\.(?P<extension>(json|xml)))?$',
                           StoryDetail.as_view(),
                           name='story_detail'),

                       # Edit story details, ex.: applicationMarvel/story/1/edit/
                       url(r'^story/(?P<pk>\d+)/edit/$',
                           UpdateView.as_view(
                               model=Story,
                               template_name='applicationMarvel/formularis/form.html',
                               form_class=StoryForm),
                           name='story_edit'),

                       # Create a story /applicationMarvel/stories/create/
                       url(r'^stories/create/$',
                           StoryCreate.as_view(),
                           name='story_create'),

                       # Delete story details, ex.: applicationMarvel/story/1/delete/
                       url(r'^story/(?P<pk>\d+)/delete/$',
                           StoryDelete.as_view(),
                           name='story_delete'),

                       # List events /applicationMarvel/events.json
                       url(r'^events(\.(?P<extension>(json|xml)))?$',
                           EventList.as_view(),
                           name='events_list'),

                       # Event details, ex.: /applicationMarvel/event/1.json
                       url(r'^event/(?P<pk>\d+)(\.(?P<extension>(json|xml)))?$',
                           EventDetail.as_view(),
                           name='event_detail'),

                       # Edit event details, ex.: applicationMarvel/event/1/edit/
                       url(r'^event/(?P<pk>\d+)/edit/$',
                           UpdateView.as_view(
                               model=Event,
                               template_name='applicationMarvel/formularis/form.html',
                               form_class=EventForm),
                           name='event_edit'),

                       # Create an event /applicationMarvel/events/create/
                       url(r'^events/create/$',
                           EventCreate.as_view(),
                           name='event_create'),

                       # Delete event details, ex.: applicationMarvel/event/1/delete/
                       url(r'^event/(?P<pk>\d+)/delete/$',
                           EventDelete.as_view(),
                           name='event_delete'),

                       # List characters /applicationMarvel/characters.json
                       url(r'characters(\.(?P<extension>(json|xml)))?$',
                           CharacterList.as_view(),
                           name='characters_list'),

                       # Character details, ex.: /applicationMarvel/character/1.json
                       url(r'^character/(?P<pk>\d+)(\.(?P<extension>(json|xml)))?$',
                           CharacterDetail.as_view(),
                           name='character_detail'),

                       # Edit character details, ex.: applicationMarvel/character/1/edit/
                       url(r'^character/(?P<pk>\d+)/edit/$',
                           UpdateView.as_view(
                               model=Character,
                               template_name='applicationMarvel/formularis/form.html',
                               form_class=CharacterForm),
                           name='character_edit'),

                       # Delete character details, ex.: applicationMarvel/event/1/delete/
                       url(r'^character/(?P<pk>\d+)/delete/$',
                           CharacterDelete.as_view(),
                           name='character_delete'),

                       # Create a character /applicationMarvel/characters/create/
                       url(r'^characters/create/$',
                           CharacterCreate.as_view(),
                           name='character_create'),
                       )

# API urls

urlpatterns += patterns('',
                        url(r'^api/$', 'api_root'),
                        url(r'^api/creators/$', APICreatorList.as_view(), name='creator_list'),
                        url(r'^api/creator/(?P<pk>\d+)/$', APICreatorDetail.as_view(), name='creator_detail'),
                        url(r'^api/stories/$', APIStoryList.as_view(), name='stories_list'),
                        url(r'^api/story/(?P<pk>\d+)/$', APIStoryDetail.as_view(), name='story_detail'),
                        url(r'^api/comics/$', APIComicList.as_view(), name='comics_list'),
                        url(r'^api/comic/(?P<pk>\d+)/$', APIComicDetail.as_view(), name='comic_detail'),
                        url(r'^api/characters/$', APICharacterList.as_view(), name='characters_list'),
                        url(r'^api/character/(?P<pk>\d+)/$', APICharacterDetail.as_view(), name='character_detail'),
                        url(r'^api/events/$', APIEventList.as_view(), name='events_list'),
                        url(r'^api/event/(?P<pk>\d+)/$', APIEventDetail.as_view(), name='event_detail'),
                        )