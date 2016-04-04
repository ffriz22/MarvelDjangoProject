from django.conf.urls import patterns, url
from django.core.urlresolvers import reverse_lazy
from django.views.generic import RedirectView

from models import Creator
from views import CreatorDetail, CreatorList

rlpatterns = patterns('',
    # Home page
    url(r'^$',
        RedirectView.as_view(url=reverse_lazy('applicationMarvel:creator_list', kwargs={'extension': 'html'})),
        name='home_page'),

    # List creators: /applicationMarvel/creator.json
    url(r'^restaurants\.(?P<extension>(json|xml|html))$',
        CreatorList.as_view(),
        name='creator_list'),

    # Creator details, ex.: /applicationMarvel/creators/1.json
    url(r'^creators/(?P<pk>\d+)\.(?P<extension>(json|xml|html))$',
        CreatorList.as_view(),
        name='creator_detail'),
)