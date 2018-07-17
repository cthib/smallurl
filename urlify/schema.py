import graphene

from graphene_django import DjangoObjectType
from urllib.request import urlopen, HTTPError, URLError

from .models import Url


class UrlType(DjangoObjectType):
    class Meta:
        model = Url


class CreateUrl(graphene.Mutation):
    class Arguments:
        long = graphene.String()

    ok = graphene.Boolean()
    url = graphene.Field(UrlType)

    @staticmethod
    def mutate(root, info, long):

        # Quick test on the given URL
        # A better solution would to give a reason for failing
        try:
            urlopen(long)
        except URLError or HTTPError:
            url = None
            ok = False
        else:
            url = Url.objects.create(long=long)
            url.set_short()
            ok = True

        return CreateUrl(url=url, ok=ok)


class UrlMutation(graphene.ObjectType):
    create_url = CreateUrl.Field()


class UrlQuery(graphene.ObjectType):
    url = graphene.Field(UrlType, long=graphene.String())
    all_urls = graphene.List(UrlType)

    def resolve_all_urls(self, info, **kwargs):
        return Url.objects.all()

    def resolve_url(self, info, **kwargs):
        long = kwargs.get('long')

        if long is not None:
            return Url.objects.get(long=long)

        return None
