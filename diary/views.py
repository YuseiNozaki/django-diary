from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView, DetailView
from django.contrib import messages
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

    def form_valid(self, form):
        messages.success(self.request, 'Notice : created post')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.warning(self.request, 'Notice : could not created post')
        return super().form_invalid(form)


class List(ListView):
    template_name = 'diary/list.html'
    model = models.Post
    

class Detail(DetailView):
    tamlate_name = 'diary/post_detail.html'
    model = models.Post
