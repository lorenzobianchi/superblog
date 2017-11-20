from django.views.generic import TemplateView, ListView, DetailView
from core.models import Post
from django.core.urlresolvers import reverse, reverse_lazy
from django.db import models, transaction
from django.shortcuts import get_object_or_404

User = get_user_model()

class ClienteList(ListView):
    model = Post
    queryset = Post.objects.all()
    template_name = "ui/home.html"
    paginate_by = 10
