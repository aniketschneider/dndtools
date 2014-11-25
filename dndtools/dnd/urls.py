# -*- coding: utf-8 -*-

from django.conf.urls.defaults import *
from django.views.generic.base import (TemplateView, RedirectView)
from dndtools.dnd.feeds import AdminLogFeed


urlpatterns = patterns(
    'dndtools.dnd.views',

    # index
    url(
        r'^$',
        'index',
        name='index',
    ),

    # Rulebooks
    (r'^rulebooks/', include('dndtools.dnd.rulebooks.urls')),

    # Feats
    (r'^feats/', include('dndtools.dnd.feats.urls')),

    # Spells
    (r'^spells/', include('dndtools.dnd.spells.urls')),

    # Classes
    (r'^classes/', include('dndtools.dnd.character_classes.urls')),

    # Skills
    (r'^skills/', include('dndtools.dnd.skills.urls')),

    # Races
    (r'^races/', include('dndtools.dnd.races.urls')),

    # Monsters
    (r'^monsters/', include('dndtools.dnd.monsters.urls')),

    # Items
    (r'^items/', include('dndtools.dnd.items.urls')),

    # Languages
    (r'^languages/', include('dndtools.dnd.languages.urls')),

    # Contacts
    (r'^contacts/', include('dndtools.dnd.contacts.urls')),

    # Rules
    (r'^rules/', include('dndtools.dnd.rules.urls')),

    # deities
    (r'^deities/', include('dndtools.dnd.deities.urls')),

    # OTHERS

    (r'^robots\.txt$', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),

    # inaccurate
    url(
        r'^inaccurate_content/$',
        'inaccurate_content',
        name='inaccurate_content',
    ),
    # inaccurate > sent
    url(
        r'^inaccurate_content/sent/$',
        'inaccurate_content_sent',
        name='inaccurate_content_sent',
    ),
    (r'^rss.xml$', AdminLogFeed()),

    # job
    url(
        r'^very_secret_url/$',
        'very_secret_url',
        name='very_secret_url',
    ),

    # MOBILE

    (r'^m/', include('dndtools.dnd.mobile.urls')),
)

urlpatterns += patterns(
    '',

    ('^contact/$', RedirectView.as_view(url='/contacts/')),
    ('^staff/$', RedirectView.as_view(url='/contacts/staff/')),
    ('^editions/$', RedirectView.as_view(url='/rulebooks/editions/')),
    ('^feat-(?P<feat_id>\d+)-(.*)\.html$', RedirectView.as_view(url='/feats/a--1/a--%(feat_id)s/')),
)
