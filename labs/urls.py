# -*- encoding: utf-8 -*-
from django.conf.urls import url

from labs.views import SubmitLab, ViewLab

urlpatterns = [
    url(r'^lab/(?P<lab_id>\d+)/submit$', SubmitLab.as_view(),
        name='submit_lab'),
    url(r'^lab/(?P<lab_id>\d+)/view$', ViewLab.as_view(),
        name='view_lab'),
]
