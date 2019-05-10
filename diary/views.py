from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView, DetailView
from . import models


class Index(TemplateView):
    template_name = 'diary/top.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class Create(CreateView):
    template_name = 'diary/create.html'
    model = models.Post
    fields = ('title', 'text')
    success_url = '/diary/list/'


class List(ListView):
    template_name = 'diary/list.html'
    model = models.Post
    

class Detail(DetailView):
    tamlate_name = 'diary/post_detail.html'
    model = models.Post
