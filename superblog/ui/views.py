from django.views.generic import TemplateView, ListView, DetailView, CreateView
from core.models import Post
from django.core.urlresolvers import reverse, reverse_lazy
from django.db import models, transaction
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect

from .forms import PostForm

class PostCreate(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'ui/post_form.html'

    def get_form_kwargs(self):
        user = self.request.user
        kwargs = super(PostCreate, self).get_form_kwargs()
        return kwargs

    def get_success_url(self):
        return reverse("post_detail", kwargs={"pk":self.kwargs['preventivo_pk']})

class HomeView(TemplateView):
    template_name = "ui/home.html"

class PostListView(ListView):
    model = Post
    queryset = Post.objects.all()
    template_name = "ui/post-list.html"

class PostDetailView(DetailView):
    model = Post
    queryset = Post.objects.all()
    template_name = "ui/post-detail.html"
