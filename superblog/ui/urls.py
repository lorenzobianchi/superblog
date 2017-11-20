from django.conf.urls import url
from . import reset_views
from .views import (
    HomeView,
)

urlpatterns = [
    url(r'^$', HomeView.as_view(), name="home"),
]
