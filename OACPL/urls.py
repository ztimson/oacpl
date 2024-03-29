import os

from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.shortcuts import Http404
from django.views.static import serve

import main.views
import case_law.views
import charter_members.views
import expert_witnesses.views
import events.views
import forum.views
import newsletters.views
import newsroom.views


@login_required
def serve_case(request, path, document_root=None, show_indexes=False):
    if not request.user.has_perm('view_pdf'):
        return Http404()
    return serve(request, path, document_root, show_indexes)


@login_required
def serve_cv(request, path, document_root=None, show_indexes=False):
    if not request.user.has_perm('view_cv'):
        return Http404()
    return serve(request, path, document_root, show_indexes)


urlpatterns = [
    url(r'^$', main.views.index, name='home'),
    url(r'^admin/logout', main.views.logout, name='logout'),
    url(r'^admin/', admin.site.urls, name='admin'),
    url(r'^attorney/(?P<id>\d+)', charter_members.views.index, name='attorney'),
    url(r'^caselaw/', case_law.views.browser, name='caselaw'),
    url(r'^contact/', main.views.contact, name='contact'),
    url(r'^experts/(?P<id>\d+)', expert_witnesses.views.viewer, name='expert'),
    url(r'^experts/', expert_witnesses.views.browser, name='experts'),
    url(r'^events/register', events.views.register, name='register'),
    url(r'^events/', events.views.view, name='events'),
    url(r'^forum/post/(?P<post>\d*)', forum.views.viewPost, name='post'),
    url(r'^forum/(?P<thread>\d*)?', forum.views.view, name='forum'),
    url(r'^login/', main.views.login, name='login'),
    url(r'^logout/', main.views.logout, name='logout'),
    url(r'^media/case_law/(?P<path>.*)$', serve_case, {'document_root': os.path.join(settings.MEDIA_ROOT, 'case_law')}, name='media caselaw'),
    url(r'^media/cv/(?P<path>.*)$', serve_cv, {'document_root': os.path.join(settings.MEDIA_ROOT, 'cv')}, name='media cv'),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}, name='media'),
    url(r'^members', charter_members.views.all, name='members'),
    url(r'^newsletter/unsubscribe', newsletters.views.unsubscribe, name='unsubscribe'),
    url(r'^newsletter/', newsletters.views.newsletters, name='newsletters'),
    url(r'^newsroom/', newsroom.views.newsroom, name='newsroom'),
    url(r'^resetToken', main.views.reset_token, name='reset token'),
    url(r'^reset/', main.views.reset, name='reset'),
    url(r'^tinymce/', include('tinymce.urls'))
]
