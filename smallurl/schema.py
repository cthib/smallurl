import graphene

from urlify import schema


schema = graphene.Schema(query=schema.UrlQuery, mutation=schema.UrlMutation)
