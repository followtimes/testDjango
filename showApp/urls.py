
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url, include
from views import showStudents

urls = [
           url(r'^students$', showStudents),
       ]