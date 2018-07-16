from django.urls import re_path

from . import views


urlpatterns = [
    re_path(r'^(?P<short_token>[0-9a-zA-Z]+)$', views.url_redirect),
]