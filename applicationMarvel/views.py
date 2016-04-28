from django.core import serializers
from django.http import HttpResponse
from django.views.generic import DetailView, ListView
from django.views.generic.base import TemplateResponseMixin
from django.views.generic.edit import CreateView
from models import Creator, Comic, Story, Event, Character
from forms import CreatorForm, CharacterForm, ComicForm, EventForm, StoryForm


class ConnegResponseMixin(TemplateResponseMixin):

    def render_json_object_response(self, objects, **kwargs):
        json_data = serializers.serialize(u"json", objects, **kwargs)
        return HttpResponse(json_data, content_type=u"application/json")

    def render_xml_object_response(self, objects, **kwargs):
        xml_data = serializers.serialize(u"xml", objects, **kwargs)
        return HttpResponse(xml_data, content_type=u"application/xml")

    def render_to_response(self, context, **kwargs):
        if 'extension' in self.kwargs:
            try:
                objects = [self.object]
            except AttributeError:
                objects = self.object_list
            if self.kwargs['extension'] == 'json':
                return self.render_json_object_response(objects=objects)
            elif self.kwargs['extension'] == 'xml':
                return self.render_xml_object_response(objects=objects)
        return super(ConnegResponseMixin, self).render_to_response(context)


class CreatorList(ListView, ConnegResponseMixin):
    model = Creator
    queryset = Creator.objects.all()
    context_object_name = 'creator_list'
    template_name = 'applicationMarvel/creator_list.html'
#end of CreatorList view


class CreatorDetail(DetailView, ConnegResponseMixin):
    model = Creator
    template_name = 'applicationMarvel/creator_detail.html'

    def get_context_data(self, **kwargs):
        context = super(CreatorDetail, self).get_context_data(**kwargs)
        return context
#end of CreatorDetail view


class CreatorCreate(CreateView):
    model = Creator
    template_name = 'applicationMarvel/formularis/form.html'
    form_class = CreatorForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreatorCreate, self).form_valid(form)


class ComicList(ListView, ConnegResponseMixin):
    model = Comic
    queryset = Comic.objects.all()
    context_object_name = 'comic_list'
    template_name = 'applicationMarvel/comic_list.html'
#end of ComicList view


class ComicDetail(DetailView, ConnegResponseMixin):
    model = Comic
    template_name = 'applicationMarvel/comic_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ComicDetail, self).get_context_data(**kwargs)
        return context
#end of ComicDetailview


class ComicCreate(CreateView):
    model = Comic
    template_name = 'applicationMarvel/formularis/form.html'
    form_class = ComicForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ComicCreate, self).form_valid(form)


class StoryList(ListView, ConnegResponseMixin):
    model = Story
    queryset = Story.objects.all()
    context_object_name = 'story_list'
    template_name = 'applicationMarvel/story_list.html'
#end of StoryList view


class StoryDetail(DetailView, ConnegResponseMixin):
    model = Story
    template_name = 'applicationMarvel/story_detail.html'

    def get_context_data(self, **kwargs):
        context = super(StoryDetail, self).get_context_data(**kwargs)
        return context
#end of StoryDetail view


class StoryCreate(CreateView):
    model = Story
    template_name = 'applicationMarvel/formularis/form.html'
    form_class = StoryForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(StoryCreate, self).form_valid(form)


class EventList(ListView, ConnegResponseMixin):
    model = Event
    queryset = Event.objects.all()
    context_object_name = 'event_list'
    template_name = 'applicationMarvel/event_list.html'
#end of EventList view


class EventDetail(DetailView, ConnegResponseMixin):
    model = Event
    template_name = 'applicationMarvel/event_detail.html'

    def get_context_data(self, **kwargs):
        context = super(EventDetail, self).get_context_data(**kwargs)
        return context
#end of EventDetail view


class EventCreate(CreateView):
    model = Event
    template_name = 'applicationMarvel/formularis/form.html'
    form_class = EventForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(EventCreate, self).form_valid(form)


class CharacterList(ListView, ConnegResponseMixin):
    model = Character
    queryset = Character.objects.all()
    context_object_name = 'character_list'
    template_name = 'applicationMarvel/character_list.html'
#end of CharacterList view


class CharacterDetail(DetailView, ConnegResponseMixin):
    model = Character
    template_name = 'applicationMarvel/character_detail.html'

    def get_context_data(self, **kwargs):
        context = super(CharacterDetail, self).get_context_data(**kwargs)
        return context
#end of CharacterDetail view


class CharacterCreate(CreateView):
    model = Character
    template_name = 'applicationMarvel/formularis/form.html'
    form_class = CharacterForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CharacterCreate, self).form_valid(form)
# Create your views here.
