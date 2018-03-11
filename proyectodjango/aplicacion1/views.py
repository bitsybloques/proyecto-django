# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.views.generic import TemplateView



# aplicaion1/views.py

class HomePageView(TemplateView):
    template_name="index.html"


# About view
class AboutPageView(TemplateView):
    template_name = "about.html"