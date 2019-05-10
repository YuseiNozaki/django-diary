from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from . import models


class Index(TemplateView):
    template_name = 'diary/top.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class List(ListView):
    template_name = 'diary/list.html'
    model = models.Post
    

class Detail(DetailView):
    tamlate_name = 'diary/post_detail.html'
    model = models.Post
    