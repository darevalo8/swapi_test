import graphene

from graphene_django.types import DjangoObjectType
from .models import Planet, People, Film, Director, Producer


class PlanetType(DjangoObjectType):
    class Meta:
        model = Planet
        interfaces = (graphene.relay.Node,)
        filter_fields = {
            'name': ['iexact', 'icontains', 'contains', 'exact'], }


class PeopleType(DjangoObjectType):
    gender = graphene.Enum('PeopleGenderEnum', People.GENDER)

    class Meta:
        model = People
        interfaces = (graphene.relay.Node,)
        filter_fields = {'name': ['iexact', 'icontains',
                                  'contains', 'exact'], 'gender': ['exact']}
        convert_choices_to_enum = False


class DirectorType(DjangoObjectType):
    class Meta:
        model = Director
        interfaces = (graphene.relay.Node,)
        filter_fields = ['name']


class ProducerType(DjangoObjectType):
    class Meta:
        model = Producer
        interfaces = (graphene.relay.Node,)
        filter_fields = ['name']


class Identity(graphene.Enum):

    EPISODE_I = Film.EPISODE_1
    EPISODE_2 = Film.EPISODE_2
    EPISODE_3 = Film.EPISODE_3
    EPISODE_4 = Film.EPISODE_4
    EPISODE_5 = Film.EPISODE_5
    EPISODE_6 = Film.EPISODE_6
    EPISODE_7 = Film.EPISODE_7
    EPISODE_8 = Film.EPISODE_8
    EPISODE_9 = Film.EPISODE_9


class FilmType(DjangoObjectType):
    episode_id = graphene.NonNull(Identity)

    class Meta:
        model = Film
        interfaces = (graphene.relay.Node,)
        filter_fields = {
            'title': ['iexact', 'icontains', 'contains', 'exact'],
            'episode_id': ['exact'],
            'release_date': ['exact']
        }
        convert_choices_to_enum = False
