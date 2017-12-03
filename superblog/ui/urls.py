from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from .views import (
    HomeView, PostListView, PostDetailView
)

urlpatterns = [
    url(r'^$', HomeView.as_view(), name="home"),
    url(r'^post-list$', PostListView.as_view(), name="post_list"),
    url(r'^post-list/(?P<pk>\d+)/detail$', PostDetailView.as_view(), name="post_detail"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
