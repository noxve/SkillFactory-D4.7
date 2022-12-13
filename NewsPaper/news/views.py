from django.shortcuts import render
from datetime import datetime
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView,  UpdateView, DeleteView
from .models import *
from .filters import PostFilter
from .forms import PostForm


class PostList(ListView):
    model = Post
    ordering = 'author'
    template_name = 'news.html'
    context_object_name = 'poste'
    paginate_by = 10


class SearchPost(ListView):
    model = Post
    template_name = 'search.html'
    context_object_name = 'search'

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class PostDetail(DetailView):
    model = Post
    template_name = 'new.html'
    context_object_name = 'post'
    pk_url_kwarg = 'pk'


class PostCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'


class PostUpdate(UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'


class PostDelete(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('news.html')



