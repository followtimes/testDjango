# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import render_to_response

# Create your views here.
def showStudents(request):
    list = [{'id': 1, 'name': 'Jack', 'age':18}, {'id': 2, 'name': 'Rose', 'age': 19}]
    return render_to_response('student.html',{'students': list})

