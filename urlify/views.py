from django.shortcuts import get_object_or_404, redirect

from .models import Url
from .base_62_converter import saturate


def url_redirect(request, short_token):
    id = saturate(short_token)
    url = get_object_or_404(Url, pk=id)

    return redirect(url.long)
