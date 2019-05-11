from django.shortcuts import render
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import (
    TemplateView,
    CreateView,
    ListView,
    DetailView,
    DeleteView,
    UpdateView,
)
from . import models


class Top(TemplateView):
    template_name = 'diary/top.html'


class Create(CreateView):
    template_name = 'diary/form.html'
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
    template_name = 'diary/detail.html'
    model = models.Post


class Update(UpdateView):
    template_name = 'diary/form.html'
    model = models.Post
    fields = ('title', 'text')

    def get_success_url(self):
        return reverse_lazy('detail', kwargs={'pk':self.kwargs['pk']})

    def form_valid(self, form):
        messages.success(self.request, 'Notice : updated post')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.warning(self.request, 'Notice : could not updated post')
        return super().form_invalid(form)



class Delete(DeleteView):
    template_name = 'diary/delete.html'
    model = models.Post
    success_url = '/diary/list/'
