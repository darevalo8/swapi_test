import graphene

from graphene_django.filter import DjangoFilterConnectionField
from app.mutations import AddOrUpdatePlanetMutation, CreatePeopleMutation
from app.types import (PlanetType, PeopleType,
                       FilmType, DirectorType, ProducerType)


class Query(graphene.ObjectType):
    planet = graphene.relay.Node.Field(PlanetType)
    all_planets = DjangoFilterConnectionField(PlanetType)

    people = graphene.relay.Node.Field(PeopleType)
    all_people = DjangoFilterConnectionField(PeopleType)

    film = graphene.relay.Node.Field(FilmType)
    all_films = DjangoFilterConnectionField(FilmType)

    director = graphene.relay.Node.Field(DirectorType)
    all_directors = DjangoFilterConnectionField(DirectorType)

    producer = graphene.relay.Node.Field(ProducerType)
    all_producers = DjangoFilterConnectionField(ProducerType)


class Mutation(graphene.ObjectType):
    add_planet_mutation = AddOrUpdatePlanetMutation.Field()
    add_people = CreatePeopleMutation.Field()
