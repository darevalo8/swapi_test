import graphene
from graphql_relay import from_global_id
from .models import Planet, People
from .types import PlanetType, PeopleType
from .utils import generic_model_mutation_process


class AddOrUpdatePlanetMutation(graphene.relay.ClientIDMutation):
    class Input:
        id = graphene.ID(required=False)
        name = graphene.String(required=True)
        rotation_period = graphene.String(required=False)
        orbital_period = graphene.String(required=False)
        diameter = graphene.String(required=False)
        climate = graphene.String(required=False)
        gravity = graphene.String(required=False)
        terrain = graphene.String(required=False)
        surface_water = graphene.String(required=False)
        population = graphene.String(required=False)

    planet = graphene.Field(PlanetType)

    @classmethod
    def mutate_and_get_payload(cls, root, info, **input):
        raw_id = input.get('id', None)
        print(f"inputtt {input['name']}")
        data = {'model': Planet, 'data': input}
        if raw_id:
            data['id'] = from_global_id(raw_id)[1]

        planet = generic_model_mutation_process(**data)

        return AddOrUpdatePlanetMutation(planet=planet)


class CreatePeopleMutation(graphene.relay.ClientIDMutation):
    class Input:
        id = graphene.ID(required=False)
        name = graphene.String(required=True)
        height = graphene.String(required=True)
        mass = graphene.String(required=True)
        hair_color = graphene.String(required=True)
        skin_color = graphene.String(required=True)
        eye_color = graphene.String(required=True)
        birth_year = graphene.String(required=True)
        gender = graphene.String(required=True)
        planet_name = graphene.String(required=True)

    people = graphene.Field(PeopleType)

    @classmethod
    def mutate_and_get_payload(cls, root, info, **input):
        try:
            planet = Planet.objects.get(name=input['planet_name'])
        except Planet.DoesNotExist:
            pass

        raw_id = input.get('id', None)
        print(f"HOLAAA {raw_id}")
        if raw_id:
            people = People.objects.get(id=from_global_id(raw_id)[1])
            if people:
                people.name = input['name']
                people.height = input['height']
                people.mass = input['mass']
                people.hair_color = input['hair_color']
                people.skin_color = input['skin_color']
                people.eye_color = input['eye_color']
                people.birth_year = input['birth_year']
                people.gender = input['gender']
                people.home_world = planet
                people.save()
        else:

            people = People(
                name=input['name'],
                height=input['height'],
                mass=input['mass'],
                hair_color=input['hair_color'],
                skin_color=input['skin_color'],
                eye_color=input['eye_color'],
                birth_year=input['birth_year'],
                gender=input['gender'],
                home_world=planet

            )
            people.save()

        return CreatePeopleMutation(people=people)
