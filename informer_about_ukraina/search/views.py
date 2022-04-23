from django.shortcuts import render
from django.views import generic


class SampleView(generic.TemplateView):
    template_name = 'search/sample.html'